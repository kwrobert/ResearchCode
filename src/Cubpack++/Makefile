SRC_DIR = Code
TMP_DIR = tmp_code

install:
	./quick_install

interface:
	./quick_itf
	mv $(TMP_DIR)/cui .
	echo 'executable "cui" is available.'

run:
	./quick_run
	mv $(SRC_DIR)/tst .
	echo 'executable "tst" is available.'

clean:
	cd $(SRC_DIR) ; /bin/rm -f *.o  tst core makefile
	cd $(SRC_DIR) ; /bin/rm -f main.c libcubpack.a
	cd $(SRC_DIR) ; /bin/rm -r -f ptrepository tempinc Templates.DB
	if test -d $(TMP_DIR); then /bin/rm -f -r $(TMP_DIR)/* ; fi
	if test -d $(TMP_DIR); then /bin/rmdir $(TMP_DIR) ; fi

