const vscode = require("vscode");
const axios = require("axios");
const { handleTestCaseGeneration } = require("./commands/testCaseCommand");
const { handleContractOptimization } = require("./commands/optimizeCommand");
const { handleTextTransform } = require("./commands/explainCommand");

function activate(context) {
	let testCaseDisposable = vscode.commands.registerCommand(
	  "file-reader.sendToBackend",
	  handleTestCaseGeneration
	);
  
	let optimizeDisposable = vscode.commands.registerCommand(
	  "file-reader.optimizeContract",
	  handleContractOptimization
	);
  
	let explainCodeDisposable = vscode.commands.registerCommand(
	  "file-reader.explainCode",
	  handleTextTransform
	);

}

function deactivate() {}

module.exports = {
  activate,
  deactivate,
};
