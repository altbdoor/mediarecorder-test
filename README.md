# mediarecorder-test

A simple GitHub Actions script that performs `MediaRecorder.isTypeSupported`
([docs](https://developer.mozilla.org/en-US/docs/Web/API/MediaRecorder/isTypeSupported_static))
on some major browsers.


## Development

To add new audio/video format to be tested, see `test.html`.

To add new browser to be tested:

1. Check if <https://github.com/browser-actions> has an action to setup the browser.
1. Add the browser details to the `matrix` in `.github\workflows\test.yml`.


## References

- <https://stackoverflow.com/questions/41739837/all-mime-types-supported-by-mediarecorder-in-firefox-and-chrome>
- <https://source.chromium.org/chromium/chromium/src/+/main:third_party/blink/renderer/modules/mediarecorder/media_recorder_handler.cc>
