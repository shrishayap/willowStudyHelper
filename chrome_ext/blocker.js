

//data from https://www.cisdem.com/resource/list-of-websites-to-block-at-work.html
var web_array = ['www.netflix.com', 'www.hulu.com', 'www.twitch.tv', 'www.disneyplus.com', 'www.vimeo.com', 'www.dailymotion.com', 'www.crunchyroll.com', 'www.fmovies.to', 'www.hbomax.com', 'www.facebook.com', 'www.twitter.com', 'www.instagram.com', 'www.reddit.com', 'www.discord.com', 'www.pinterest.com', 'www.tiktok.com', 'www.tumblr.com', 'www.reddit.com', 'www.amazon.com', 'www.amazon.ca', 'www.ebay.com', 'www.walmart.com', 'www.etsy.com', 'www.target.com', 'www.costco.com', 'www.bestbuy.com', 'www.newegg.com', 'www.wish.com', 'www.wayfair.com', 'www.tinder.com', 'www.match.com', 'www.pof.com', 'www.okcupid.com', 'www.zoosk.com', 'www.bumble.com', 'www.seeking.com', 'www.happn.com', 'www.cs-online.club', 'www.worldofsolitaire.com', 'www.pogo.com', 'www.miniclip.com', 'www.addictinggames.com'];

var len_array = web_array.length;

var link = window.location.hostname;

function replace_page(host_name) {
    document.body.innerHTML = host_name;
    return 0;
};

for (var i = 0; i < len_array; i ++) {
    if (link == web_array[i]) {
        replace_page(web_array[i]);
        send_neg();
    };
};

function send_neg() {

    const Http = new XMLHttpRequest();
    const url = 'http://127.0.0.1:5000/banned_web_attempt';
    Http.open("POST", url, true);
    Http.send('breach=true');

    Http.onreadystatechange = (e) => {
        console.log(Http.responseText)
    }

};

document.addEventListener('DOMContentLoaded', function() {
    var link = document.getElementById('submit');
    link.addEventListener('click', function() {
        let username = document.getElementById('username').value;
        let myNewUrl = 'http://127.0.0.1:5000/study?username=' + username;
        chrome.tabs.update(undefined, { url: myNewUrl });

    });
});