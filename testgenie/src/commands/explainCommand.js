const vscode = require("vscode");

async function handleTextTransform() {
  const editor = vscode.window.activeTextEditor;
  if (!editor) {
    return;
  }

  const selection = editor.selection;
  const selectedText = editor.document.getText(selection);

  if (selectedText) {
    await editor.edit((editBuilder) => {
      editBuilder.replace(selection, selectedText.toUpperCase());
    });
  } else {
    vscode.window.showInformationMessage("No text selected!");
  }
}

module.exports = {
  handleTextTransform,
};
