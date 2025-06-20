export const getClearObjectFields = (object: Object): Object => Object.keys(object).reduce((prev, k) => {
  if (object[k] !== null && object[k] !== undefined) {
    prev[k] = object[k];
  }

  return prev;
}, {})