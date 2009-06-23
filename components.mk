# browser-qt

alterator/design/bg.png: images/installer.png
	convert $< -resize '800x600!' -fill '#c62530' -font /usr/share/fonts/ttf/dejavu/DejaVuSansCondensed-Bold.ttf -style Normal -weight Normal -pointsize 20 -gravity northeast -draw 'text 25,25 "$(STATUS)"' $@

browser-qt:alterator/design/bg.png
	install -d $(datadir)/alterator-browser-qt/design
	cd alterator; rcc-qt4 -binary theme.qrc -o $(datadir)/alterator-browser-qt/design/$(THEME).rcc; cd -
	install -d $(sysconfdir)/alternatives/packages.d
	printf '/etc/alterator/design-browser-qt\t/usr/share/alterator-browser-qt/design/$(THEME).rcc\t50\n'>$(sysconfdir)/alternatives/packages.d/$(THEME).rcc

# ahttpd

ahttpd:
	install -d $(datadir)/alterator/design/styles
	cp -a alterator/images $(datadir)/alterator/design
	cp -a alterator/styles/*.css $(datadir)/alterator/design/styles
