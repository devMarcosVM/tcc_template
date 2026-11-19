GREEN = \033[92m
END = \033[0m

.PHONY: build
build:
	docker compose build latex
.PHONY: pdf
pdf:
	@if [ -f latex/figuras/figuras.zip ]; then unzip -n -q latex/figuras/figuras.zip -d latex/figuras; fi
	@if command -v latexmk >/dev/null 2>&1; then \
		$(MAKE) -C latex; \
	else \
		docker compose run --rm --user "$$(id -u):$$(id -g)" latex make; \
	fi
	cp -f ./latex/build/TCC_PDF.pdf ./TCC_PDF.pdf
	@echo "$(GREEN)PDF gerado com sucesso.$(END)"
.PHONY: clean
clean:
	cd latex && make clean
hooks:
	chmod +x ./.githooks/post-commit.sh
	ln -f ./.githooks/post-commit.sh .git/hooks/post-commit