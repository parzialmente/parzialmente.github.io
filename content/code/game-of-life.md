Title: Game of Life in Javascript

[Gioco della vita](http://it.wikipedia.org/wiki/Gioco_della_vita) di
John Conway scritto in Javascript e disegnato sul `canvas` HTML.

Click per brulicare, click per fermare, doppio click per ricominciare.

Quando si dice l'essenzialità.

Il [codice su GitHub](https://github.com/rjack/game-of-life) è
cristallizzato su un laconico _sketching the UI_, ennesima prova che
scrivere le GUI è una grandissima rottura di scatole.

<canvas id="canvas"></canvas>

<script type="text/javascript" src="/static/js/game-of-life/grid.js"></script>
<script type="text/javascript" src="/static/js/game-of-life/graphics.js"></script>
<script type="text/javascript" src="/static/js/game-of-life/game-of-life.js"></script>
<script type="text/javascript">
(function () {
	// TODO: give a decent initial configuration instead of null (random)
	GOL.init(320, 240, 1, 1, null);
	var cnv = document.getElementById("canvas");
	var running = false;
	cnv.addEventListener("click", function () {
		running = !running
		if (running) {
			GOL.start();
		} else {
			GOL.stop();
			}
	}, false);
	cnv.addEventListener("dblclick", function () {
		// http://stackoverflow.com/a/880518/54967
		if (document.selection && document.selection.empty) {
			document.selection.empty();
		} else if (window.getSelection) {
			window.getSelection().removeAllRanges();
		}
		if (running) {
			running = false;
			GOL.stop();
		}
		GOL.init(320, 240, 1, 1, null);
	}, false);
}())
</script>
