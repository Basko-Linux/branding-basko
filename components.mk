# browser-qt

components/browser-qt/design/bg.png: images/installer.png
	convert $< -resize '800x600!' -fill '#c62530' -font /usr/share/fonts/ttf/dejavu/DejaVuSansCondensed-Bold.ttf -style Normal -weight Normal -pointsize 20 -gravity northeast -draw 'text 25,25 "$(STATUS)"' $@

browser-qt:components/browser-qt/design/bg.png
	install -d $(datadir)/alterator-browser-qt/design
	cd components/browser-qt; rcc-qt4 -binary theme.qrc -o $(datadir)/alterator-browser-qt/design/$(THEME).rcc; cd -
	install -d $(sysconfdir)/alternatives/packages.d
	printf '/etc/alterator/design-browser-qt\t/usr/share/alterator-browser-qt/design/$(THEME).rcc\t50\n'>$(sysconfdir)/alternatives/packages.d/$(THEME).rcc

# ahttpd

ahttpd:
	install -d $(datadir)/alterator/design/styles
	cp -a components/ahttpd/images $(datadir)/alterator/design
	[ ! -f images/logo.png ] || convert images/logo.png -fill '#ffffff' -font /usr/share/fonts/ttf/dejavu/DejaVuSans-Bold.ttf -style Normal -weight Normal -pointsize 24 -gravity northwest -draw 'text 0,0 "$(VERSION) $(NAME)"' $(datadir)/alterator/design/images/logo.png
	cp -a components/ahttpd/styles/*.css $(datadir)/alterator/design/styles

# bootloader and bootsplash
boot:
	cp -a  /usr/src/design-bootloader-source ./
	cp -a components/bootloader/config design-bootloader-source/
	cp -a components/bootloader/gfxboot.cfg design-bootloader-source/data-install/
	cp -a components/bootloader/gfxboot.cfg design-bootloader-source/data-boot/
	for size in 1024x768 800x600 640x480; do \
		convert images/boot.jpg -resize "$$size!" -fill '#c62530' -font /usr/share/fonts/ttf/dejavu/DejaVuSansCondensed-Bold.ttf -style Normal -weight Normal -pointsize 20 -gravity northeast -draw 'text 25,25 "@STATUS@"' boot-$$size.jpg ;\
		cp -al boot-$$size.jpg components/bootsplash/images/silent-$$size.jpg ;\
		convert -resize "$$size!" images/console.jpg components/bootsplash/images/bootsplash-$$size.jpg;\
	done
	cp -al boot-800x600.jpg design-bootloader-source/data-boot/back.jpg
	cp -al boot-800x600.jpg design-bootloader-source/data-install/back.jpg
#bootsplash
	mkdir -p $(sysconfdir)/bootsplash/themes/$(THEME)
	cp -a components/bootsplash/* $(sysconfdir)/bootsplash/themes/$(THEME)
#bootloader
	DEFAULT_LANG='--lang-to-subst--' PATH=$(PATH):/usr/sbin make -C design-bootloader-source
	install -d -m 755  $(sysconfdir)/../boot/splash/$(THEME)
	install -d -m 755 $(datadir)/gfxboot/$(THEME)
	install -m 644 design-bootloader-source/message $(sysconfdir)/../boot/splash/$(THEME)
	install -m 644 design-bootloader-source/bootlogo $(datadir)/gfxboot/$(THEME)
