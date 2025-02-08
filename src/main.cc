#include <cstdlib>
#include <iostream>
#include <string>

int main(int argc, char *argv[]) {
  if (argc < 2) {
    std::cerr << "Usage: ask \"your question here\"" << std::endl;
    return 1;
  }

  std::string query;
  for (int i = 1; i < argc; ++i) {
    query += argv[i];
    if (i < argc - 1)
      query += " ";
  }

  std::string sender = "python3 src/caller.py \"" + query + "\"";
  int result = std::system(sender.c_str());

  return result;
}
