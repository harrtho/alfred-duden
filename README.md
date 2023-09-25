# Duden Alfred Workflow

[![GitHub Version][shield-version]][gh-releases]
[![GitHub All Releases][shield-downloads]][gh-releases]
[![GitHub][shield-license]][license-mit]

Search the definitive German dictionary at [Duden.de][duden] with auto-suggest in [Alfred][alfred].

![][preview]

## Download & Installation

Download the [latest workflow release][gh-latest-release] from GitHub. Open the workflow file to
install in Alfred.

## Usage

Default keyword is `duden`. Enter your query after that.

Actioning a result with `RETURN` will open the full results page at duden.de in
your browser. Pressing `⌘` on a result will show the URL in its subtitle.

You can also assign a Hotkey (keyboard shortcut) that will look up the currently
selected text in any application.

## Bug Reports and Feature Requests

Please use [GitHub issues][gh-issues] to report bugs or request features.

## Contributors

This Alfred Workflow comes from the [abandoned Workflow][abandoned-workflow] of
[Dean Jackson][deanishe]

## License

Duden Alfred Workflow is licensed under the [MIT License][license-mit]

The workflow uses the following libraries:

- [Beautiful Soup][bs] ([MIT License][license-mit])
- [html5lib][h5l] ([MIT License][license-mit])
- [Alfred-PyWorkflow][alfred-pyworkflow] ([MIT License][license-mit])

[abandoned-workflow]: https://github.com/deanishe/alfred-duden
[alfred-pyworkflow]: https://www.github.com/harrtho/alfred-pyworkflow/
[alfred]: https://www.alfredapp.com/
[bs]: https://www.crummy.com/software/BeautifulSoup/
[deanishe]: https://github.com/deanishe
[duden]: https://www.duden.de/woerterbuch
[gh-issues]: https://github.com/harrtho/alfred-duden/issues
[gh-latest-release]: https://github.com/harrtho/alfred-duden/releases/latest
[gh-releases]: https://github.com/harrtho/alfred-duden/releases
[h5l]: https://github.com/html5lib/html5lib-python
[license-mit]: https://opensource.org/licenses/MIT
[preview]: img/preview.png
[shield-downloads]: https://img.shields.io/github/downloads/harrtho/alfred-duden/total.svg
[shield-license]: https://img.shields.io/github/license/harrtho/alfred-duden.svg
[shield-version]: https://img.shields.io/github/release/harrtho/alfred-duden.svg
