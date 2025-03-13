const vscode = require("vscode");
const yaml = require("js-yaml");
const path = require("path");

function parseFile(documentText, fileExtension) {
  if (fileExtension === ".json") {
    return JSON.parse(documentText);
  }
  return yaml.load(documentText);
}

function validateFileExtension(fileName) {
  const fileExtension = path.extname(fileName).toLowerCase();
  if (![".json", ".yaml", ".yml"].includes(fileExtension)) {
    throw new Error("Please open a JSON or YAML file");
  }
  return fileExtension;
}

function getActiveEditor() {
  const editor = vscode.window.activeTextEditor;
  if (!editor) {
    throw new Error("No active editor found");
  }
  return editor;
}

module.exports = {
  parseFile,
  validateFileExtension,
  getActiveEditor,
};
