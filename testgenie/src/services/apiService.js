const axios = require("axios");

async function generateTestCases(contract, language) {
  const response = await axios.post(
    "http://localhost:8000/gemini-prompt",
    {
      contract: JSON.stringify(contract),
      language,
    },
    {
      headers: {
        "Content-Type": "application/json",
      },
    }
  );
  return response.data;
}

async function optimizeContract(contract) {
  const response = await axios.post(
    "http://localhost:8000/optimize-contract",
    {
      contract: JSON.stringify(contract),
    },
    {
      headers: {
        "Content-Type": "application/json",
      },
    }
  );
  return response.data;
}

module.exports = {
  generateTestCases,
  optimizeContract,
};
