def countItems(a: list) -> int:
  if len(a) == 0:
    return 0
  else:
    return 1 + countItems(a[1:])
