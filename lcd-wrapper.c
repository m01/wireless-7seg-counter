#include <stdlib.h>
#include <unistd.h>

int main() {
  setuid(0);
  setgid(0);
	system("whoami");
	system("python /path/to/lcd.py");
	exit(0);
}

