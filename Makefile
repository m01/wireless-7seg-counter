lcd-wrapper: lcd-wrapper.c
	gcc -o lcd-wrapper lcd-wrapper.c

clean:
	rm -f lcd-wrapper
