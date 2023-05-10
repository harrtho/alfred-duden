# Duden.de search workflow for Alfred

[![GitHub Version][version-shield]][releases]
[![GitHub All Releases][downloads-shield]][releases]
[![GitHub][license-shield]][mit-license]

A workflow for [Alfred 5][alfred].

Search the definitive German dictionary at [Duden.de][duden] with auto-suggest.

![Workflow in action][demo]

## Download and installation

Download the Workflow from the [GitHub releases page][releases] and double-click
the `Duden-Search-XXX.alfredworkflow` file to install.

## Usage

Default keyword is `duden`. Enter your query after that.

Actioning a result with `RETURN` will open the full results page at duden.de in
your browser. Pressing `⌘` on a result will show the URL in its subtitle.

You can also assign a Hotkey (keyboard shortcut) that will look up the currently
selected text in any application.

## Feedback

If you have a feature request, bug report or other query, you can get in touch
using the [GitHub issue tracker][issues] or [the Alfred Forum page][forum].

## Licensing, thanks

The code of this workflow is released under the [MIT license][mit-license].

This workflow is based on the following libraries (also released under the MIT license):

- The legendary [Beautiful Soup][bs] by [Leonard Richardson][lenny],
- the extremely awesome [html5lib][h5l] by [James Graham][jgraham] & co. and
- the not entirely useless [Alfred-PyWorkflow][alfred-pyworkflow] by [deanishe][deanishe] and [me][harrtho].

[alfred]: https://www.alfredapp.com/
[alfred-pyworkflow]: https://www.github.com/harrtho/alfred-pyworkflow/
[bs]: https://www.crummy.com/software/BeautifulSoup/
[deanishe]: https://github.com/deanishe/
[demo]: https://raw.githubusercontent.com/harrtho/alfred-duden/master/demo.gif "Workflow in action"
[downloads-shield]: https://img.shields.io/github/downloads/harrtho/alfred-duden/total.svg
[duden]: https://www.duden.de/woerterbuch
[forum]: https://www.alfredforum.com/topic/4707-duden-dictionary-search-with-auto-suggest/
[h5l]: https://github.com/html5lib/html5lib-python
[harrtho]: https://github.com/harrtho/
[issues]: https://github.com/harrtho/alfred-duden/issues
[jgraham]: https://github.com/jgraham
[lenny]: https://www.crummy.com/self/
[license-shield]: https://img.shields.io/github/license/harrtho/alfred-duden.svg
[mit-license]: https://opensource.org/licenses/MIT
[releases]: https://github.com/harrtho/alfred-duden/releases
[version-shield]: https://img.shields.io/github/release/harrtho/alfred-duden.svg
