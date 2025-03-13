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
  
}

module.exports = {
  handleTestCaseGeneration,
};
