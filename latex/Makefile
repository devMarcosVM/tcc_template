TARGET = build/TCC_PDF.pdf
VERSION = 0.1.0

FIXOS_DIR = fixos
FIXOS_SOURCES = informacoes.tex fichaCatalografica.tex \
		folhaDeAprovacao.tex pacotes.tex comandos.tex setup.tex	\
		listasAutomaticas.tex indiceAutomatico.tex

FIXOS_FILES = $(addprefix $(FIXOS_DIR)/, $(FIXOS_SOURCES))

EDITAVEIS_DIR = editaveis
EDITAVEIS_SOURCES = informacoes.tex errata.tex dedicatoria.tex \
					agradecimentos.tex epigrafe.tex resumo.tex abstract.tex \
					abreviaturas.tex simbolos.tex \
					introducao.tex \
					referencial-teorico.tex \
					suporte.tex \
					metodologia.tex \
					proposta.tex \
					resultados.tex \
					aspectosgerais.tex consideracoes.tex textoepostexto.tex \
					elementosdotexto.tex elementosdopostexto.tex \
					apendices.tex anexos.tex

EDITAVEIS_FILES = $(addprefix $(EDITAVEIS_DIR)/, $(EDITAVEIS_SOURCES))

MAIN_FILE = tcc.tex
SOURCES = $(FIXOS_FILES) $(EDITAVEIS_FILES)

.PHONY: all clean dist-clean

all:
	mkdir -p build
	latexmk -pdf -shell-escape -interaction=nonstopmode -halt-on-error -outdir=build -jobname=TCC_PDF $(MAIN_FILE)

clean:
	latexmk -c -outdir=build -jobname=TCC_PDF $(MAIN_FILE)

dist: clean
	tar vczf tcc-fga-latex-$(VERSION).tar.gz *

dist-clean: clean
	rm -f $(TARGET)
