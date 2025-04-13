function duplicateCharacters(str: str): string[] {
  const charCount: { [key: string]: number } = {};
  const duplicates: string[] = [];

  for (const char of str) {
    charCount[char] = (charCount[char] || 0) + 1;
  }

  for (const char in charCount) {
    if (charCount[char] > 1) {
      duplicates.push(char);
    }
  }

  return duplicates;
}