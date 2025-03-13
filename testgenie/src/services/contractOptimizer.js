function optimizeSwaggerContract(contract) {
  const optimizedContract = JSON.parse(JSON.stringify(contract));

  if (optimizedContract.paths) {
    const newPaths = {};
    for (const [path, methods] of Object.entries(optimizedContract.paths)) {
      let optimizedPath = path.toLowerCase();

      optimizedPath = optimizedPath.replace(
        /\/([a-z]+)($|\/)/g,
        (match, resource, ending) => {
          if (resource.endsWith("s")) return match;
          if (resource.endsWith("y"))
            return `/${resource.slice(0, -1)}ies${ending}`;
          return `/${resource}s${ending}`;
        }
      );

      newPaths[optimizedPath] = methods;
    }
    optimizedContract.paths = newPaths;
  }

  if (optimizedContract.paths) {
    for (const pathItem of Object.values(optimizedContract.paths)) {
      for (const method of Object.values(pathItem)) {
        if (method.operationId) {
          method.operationId = method.operationId
            .replace(/([a-z])([A-Z])/g, "$1-$2")
            .toLowerCase();
        }

        if (method.tags) {
          method.tags = method.tags.map((tag) =>
            tag.toLowerCase().replace(/\s+/g, "-")
          );
        }
      }
    }
  }

  return optimizedContract;
}

module.exports = {
  optimizeSwaggerContract,
};
