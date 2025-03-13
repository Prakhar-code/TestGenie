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
  
}

module.exports = {
  handleContractOptimization,
};
