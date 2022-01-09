# browser-qt

components/browser-qt/design/bg.png: images/installer.png
	convert $< -resize '800x600!' -fill '#857b7b' -font /usr/share/fonts/ttf/dejavu/DejaVuSansCondensed-Bold.ttf -style Normal -weight Normal -pointsize 20 -gravity northeast -draw 'text 25,25 "$(STATUS)"' $@

browser-qt:components/browser-qt/design/bg.png
	install -d $(datadir)/alterator-browser-qt/design
	cd components/browser-qt; rcc-qt5 -binary theme.qrc -o $(datadir)/alterator-browser-qt/design/$(THEME).rcc; cd -
	install -d $(sysconfdir)/alternatives/packages.d
	printf '/etc/alterator/design-browser-qt\t/usr/share/alterator-browser-qt/design/$(THEME).rcc\t49\n'>$(sysconfdir)/alternatives/packages.d/$(THEME).rcc

# ahttpd

ahttpd:
	for i in components/ahttpd/images/*.svg; do \
	    image=$${i%.svg}; \
	    convert -background none $$image.svg $$image.png ; \
	done
	install -d $(datadir)/alterator/design/styles
	cp -a components/ahttpd/images $(datadir)/alterator/design
	install -Dpm644 images/product-logo.png $(datadir)/alterator/design/images/product-logo.png
	cp -a components/ahttpd/styles/*.css $(datadir)/alterator/design/styles

# bootloader and bootsplash
boot-images:
	cp -a  /usr/src/design-bootloader-source ./
	cp -a components/bootloader/config design-bootloader-source/
	cp -a components/bootloader/gfxboot.cfg design-bootloader-source/data-install/
	cp -a components/bootloader/gfxboot.cfg design-bootloader-source/data-boot/
	for size in 1024x768 800x600 640x480; do \
		convert images/boot.png -quality 97 -resize "$$size!" -fill '#c62530' -font /usr/share/fonts/ttf/dejavu/DejaVuSansCondensed-Bold.ttf -style Normal -weight Normal -pointsize 20 -gravity northeast -draw 'text 25,25 "$(STATUS)"' boot-$$size.jpg ;\
	done
	convert images/boot.png -resize "800x600!" -fill '#c62530' -font /usr/share/fonts/ttf/dejavu/DejaVuSansCondensed-Bold.ttf -style Normal -weight Normal -pointsize 20 -gravity northeast -draw 'text 25,25 "$(STATUS)"' design-bootloader-source/data-install/back.jpg
	convert -colorspace YCbCr -sampling-factor 2x2 images/boot.png JPEG:images/boot.jpg
	cp -al images/boot.jpg design-bootloader-source/data-boot/back.jpg
	cp -afl images/boot.jpg design-bootloader-source/data-install/back.jpg
	mv design-bootloader-source/data-install/back{,.1}.jpg
	convert -quality 97 -fill '#acdaf2' -draw 'rectangle 0,0,2,2' design-bootloader-source/data-install/back{.1,}.jpg
	rm -f design-bootloader-source/data-install/back.*.jpg

# bootloader and bootsplash
boot: boot-images
	cp -a  /usr/src/design-bootloader-source ./
	cp -a components/bootloader/config design-bootloader-source/
# enable mediacheck by default... argh
	sed -i '/^\/iso\.needscheck {$$/,/^} def$$/ s/  false/  true/' design-bootloader-source/src/common.inc
	cp -a components/bootloader/gfxboot.cfg design-bootloader-source/data-install/
	cp -a components/bootloader/gfxboot.cfg design-bootloader-source/data-boot/
	for size in 1024x768 800x600 640x480; do \
		convert images/boot.jpg -quality 97 -resize "$$size!" -fill '#857b7b' -font /usr/share/fonts/ttf/dejavu/DejaVuSansCondensed-Bold.ttf -style Normal -weight Normal -pointsize 20 -gravity northeast -draw 'text 25,25 "$(STATUS)"' boot-$$size.jpg ;\
	done
	cp -afl boot-800x600.jpg design-bootloader-source/data-boot/back.jpg
	cp -afl boot-800x600.jpg design-bootloader-source/data-install/back.jpg
#bootsplash
	mkdir -p $(datadir)/plymouth/themes/$(THEME)
#	cp -afl boot-800x600.jpg $(datadir)/plymouth/themes/$(THEME)/grub.jpg
	cp -afl images/background*x*.png $(datadir)/plymouth/themes/$(THEME)/
#	cp -afl images/wallpaper.png $(datadir)/plymouth/themes/$(THEME)/wallpaper.png
	cp -af components/bootsplash/* $(datadir)/plymouth/themes/$(THEME)
	mv $(datadir)/plymouth/themes/$(THEME)/theme.plymouth $(datadir)/plymouth/themes/$(THEME)/$(THEME).plymouth
	rm -f $(datadir)/plymouth/themes/$(THEME)/*.in
#bootloader
ifeq (,$(filter-out i586 i686 x86_64,$(ARCH)))
	DEFAULT_LANG='--lang-to-subst--' PATH=$(PATH):/usr/sbin make -C design-bootloader-source
	install -d -m 755 $(datadir)/gfxboot/$(THEME)
	install -m 644 design-bootloader-source/bootlogo $(datadir)/gfxboot/$(THEME)
endif
#grub2
	convert -size 16x16 -define png:color-type=2 -depth 8 xc:'#798491' components/grub2/selected_blob_c.png
	install -d -m 755  $(sysconfdir)/../boot/grub/themes/$(THEME)
	cp -a components/grub2/* $(sysconfdir)/../boot/grub/themes/$(THEME)/
	install -m 644 images/boot.png $(sysconfdir)/../boot/grub/themes/$(THEME)/boot.png
#	install -m 644 images/boot.jpg $(sysconfdir)/../boot/grub/themes/$(THEME)/grub.jpg

# index html page, start page for all local browsers
INDEXHTML_DIR=$(datadir)/doc/indexhtml
indexhtml:
	for i in notes/index*.html components/indexhtml/*.css;do \
	  install -Dpm644 $$i $(INDEXHTML_DIR)/`basename $$i`; \
	done
	install -Dpm644 /dev/null $(INDEXHTML_DIR)/index.html
	cp -a components/indexhtml/img $(INDEXHTML_DIR)
	install -Dpm644 images/product-logo.png $(INDEXHTML_DIR)/img/product-logo.png
	install -Dpm644 components/indexhtml/indexhtml.desktop $(datadir)/applications/indexhtml.desktop
