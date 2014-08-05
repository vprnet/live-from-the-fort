var LFTF = LFTF || {};

LFTF.init = function() {
    var autoplay = window.location.search.substring(1);
    if (autoplay === 'autoplay') {
        var youTubeFrame = $('iframe.band_video'),
            youTubeSrc = youTubeFrame.attr('src');

        youTubeFrame.attr('src', youTubeSrc + '&autoplay=1');
    }
};

LFTF.init();
