#include <cstdlib>
#include <iostream>
#include <string>

int main (int argc, char *argv[]) {

  std::string sender = std::string("python3 caller.py ") + argv[1];
  std::system(sender.c_str());

  return 0;
}

