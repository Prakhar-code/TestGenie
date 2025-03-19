const vscode = require("vscode");
const path = require("path");
const yaml = require("js-yaml");
const {
  parseFile,
  validateFileExtension,
  getActiveEditor,
} = require("../utils/fileUtils");
const { optimizeSwaggerContract } = require("../services/contractOptimizer");
const { optimizeContract } = require("../services/apiService");

async function handleContractOptimization() {
  try {
    const editor = getActiveEditor();
    const fileName = editor.document.fileName;
    const fileExtension = validateFileExtension(fileName);
    const documentText = editor.document.getText();
    const parsedContent = parseFile(documentText, fileExtension);

    const locallyOptimizedContract = optimizeSwaggerContract(parsedContent);

    await vscode.window.withProgress(
      {
        location: vscode.ProgressLocation.Notification,
        title: "Optimizing API contract ...",
        cancellable: true,
      },
      async () => {
        const finalOptimizedContract = await optimizeContract(
          locallyOptimizedContract
        );

        let optimizedContent;
        if (fileExtension === ".json") {
          optimizedContent = JSON.stringify(finalOptimizedContract, null, 2);
        } else {
          optimizedContent = yaml.dump(finalOptimizedContract, {
            indent: 2,
            lineWidth: -1,
          });
        }

        const optimizedFilePath = vscode.Uri.file(
          path.join(
            path.dirname(fileName),
            `${path.basename(
              fileName,
              fileExtension
            )}_optimized${fileExtension}`
          )
        );

        const workspaceEdit = new vscode.WorkspaceEdit();
        workspaceEdit.createFile(optimizedFilePath, { overwrite: true });
        await vscode.workspace.applyEdit(workspaceEdit);

        const optimizedDoc = await vscode.workspace.openTextDocument(
          optimizedFilePath
        );
        const optimizedEditor = await vscode.window.showTextDocument(
          optimizedDoc
        );
        await optimizedEditor.edit((editBuilder) => {
          editBuilder.insert(new vscode.Position(0, 0), optimizedContent);
        });

        vscode.window.showInformationMessage(
          "Successfully optimized the API Contract"
        );
      }
    );
  } catch (error) {
    vscode.window.showErrorMessage(`Error: ${error.message}`);
  }
}

module.exports = {
  handleContractOptimization,
};
