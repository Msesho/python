def futureValue(x, i, n, comp):
  fv = (x * (1 + i) ** n - x) / i;
  switch (comp) {
    case "monthly":
      n = n * 12;
      i = (i / 100) / 12;
    case "quarterly":
      n = n * 4;
      i = (i / 100) / 4;
    case "half-yearly", "biennial":
      n = n * 2;
      i = (i / 100) / 2;
    default:
      n = n * 1;
      i = i / 100;
  }
  return fv
