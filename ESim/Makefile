CC = g++
CFLAGS = -lm -pthread -Ofast -march=native -Wall -funroll-loops -Wno-unused-result -lgsl -lm -lgslcblas
LFLAGS = -lgsl -lm -lgslcblas
INCLUDES = -I/usr/local/include -Ieigen-3.3.3
LIBS = -L/usr/local/lib

BIN = bin/esim bin/search

all: bin $(BIN)

bin:
	mkdir bin
	
bin/search : bin/ransampl.o bin/linelib.o bin/main.o src/search.cpp bin
	$(CC) $(CFLAGS) src/search.cpp -o bin/search $(INCLUDES) $(LIBS) $(LFLAGS)

bin/esim : bin/ransampl.o bin/linelib.o bin/main.o src/search.cpp bin
	$(CC) $(CFLAGS) -o bin/esim bin/ransampl.o bin/linelib.o bin/main.o $(INCLUDES) $(LIBS) $(LFLAGS)

bin/ransampl.o : src/ransampl.c bin
	$(CC) $(CFLAGS) -c src/ransampl.c $(INCLUDES) $(LIBS) $(LFLAGS) -o bin/ransampl.o

bin/linelib.o : src/linelib.cpp src/ransampl.h bin
	$(CC) $(CFLAGS) -c src/linelib.cpp $(INCLUDES) $(LIBS) $(LFLAGS) -o bin/linelib.o

bin/main.o : src/main.cpp bin/linelib.o bin
	$(CC) $(CFLAGS) -c src/main.cpp $(INCLUDES) $(LIBS) $(LFLAGS) -o bin/main.o

clean :
	rm -rf bin
