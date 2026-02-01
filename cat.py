'''
This program prints stdin to the screen.
'''
import sys

def cat(file):
    buf = bytearray(4096)
    mv = memoryview(buf)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            if filename == "-":
                cat(sys.stdin.buffer)
            else:
                with open(filename, "rb") as f:
                    cat(f)
    else:
        cat(sys.stdin.buffer)
