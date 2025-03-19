const vscode = require("vscode");
const path = require("path");
const { LANGUAGE_FILE_EXTENSIONS } = require("../constants");
const {
  parseFile,
  validateFileExtension,
  getActiveEditor,
} = require("../utils/fileUtils");
const { generateTestCases } = require("../services/apiService");

async function handleTestCaseGeneration() {
  try {
    const editor = getActiveEditor();
    const fileName = editor.document.fileName;
    const fileExtension = validateFileExtension(fileName);
    const documentText = editor.document.getText();
    const parsedContent = parseFile(documentText, fileExtension);

    const selectedLanguage = await vscode.window.showQuickPick(
      ["python", "nodejs", "java"],
      {
        placeHolder: "Select the language for test cases",
      }
    );

    if (!selectedLanguage) {
      throw new Error("Language selection is required");
    }

    await vscode.window.withProgress(
      {
        location: vscode.ProgressLocation.Notification,
        title: "Generating test cases...",
        cancellable: true,
      },
      async () => {
        const testCaseContent = await generateTestCases(
          parsedContent,
          selectedLanguage
        );
        const fileExt = LANGUAGE_FILE_EXTENSIONS[selectedLanguage];

        const workspaceEdit = new vscode.WorkspaceEdit();
        const testFilePath = vscode.Uri.file(
          path.join(path.dirname(fileName), `test_cases.${fileExt}`)
        );

        workspaceEdit.createFile(testFilePath, { overwrite: true });
        await vscode.workspace.applyEdit(workspaceEdit);

        const testFileDoc = await vscode.workspace.openTextDocument(
          testFilePath
        );
        const editor = await vscode.window.showTextDocument(testFileDoc);
        await editor.edit((editBuilder) => {
          editBuilder.insert(new vscode.Position(0, 0), testCaseContent);
        });

        vscode.window.showInformationMessage(
          "Successfully generated test cases"
        );
      }
    );
  } catch (error) {
    vscode.window.showErrorMessage(`Error: ${error.message}`);
  }
}

module.exports = {
  handleTestCaseGeneration,
};
