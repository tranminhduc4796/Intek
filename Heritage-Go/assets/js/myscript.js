// Ready function to load code
$(document).ready(function () {
    // Get photos form HeritageService
    limit = 5;
    update_content($('.posts'), limit, {
        offset: offset
    });
    offset = limit;
});




function showHidePassword() {
    var x = document.getElementById("userPW");
    if (x.type === "password") {
        x.type = "text";
        document.getElementById("lock-icon").className = "fas fa-unlock-alt lock"
    } else {
        x.type = "password";
        document.getElementById("lock-icon").className = "fas fa-lock lock"

    }
}

// VARIABLES
var offset;
const elements_contain_event = [
    'fa',
    'post-translate',
    'post-btn',
    'post-translate post-translate--shake',
    'language_name',
    'language-input',
];
const article_container = $('#post-container');
article_container.hide();

function update_heritage_data(article_container_clone, photo) {
    // Display data to index.html
    // Heritage photograph
    article_container_clone.find('.post__img').attr('src', 'https:' + photo['image_url'] + '?size=medium');
    // User avatar
    article_container_clone.find('.user-avt').attr("src", 'https:' + photo['account']['picture_url']);
    // Caption
    article_container_clone.find('.info__caption--text').text(photo['title'][0]['content']);
    // Area user local
    article_container_clone.find('.location__name').text(photo['area_name']);
    // Taken year
    article_container_clone.find('.year--canchange').text(photo['capture_time'] || 'N/A');
    article_container_clone.attr('id', photo['photo_id']);
    article_container_clone.show();
    return article_container_clone;
}

function update_content(selected_section, limit, {
    offset = 0
}) {
    mHeritageGoService.getPhotos({
        limit: limit,
        offset: offset
    }).then(function (photos) {
        var count = 0;
        $(photos).each(function () {
            // Retrieve detail of a photo
            mHeritageGoService.getPhoto(this).then(function (photo) {
                var article_container_clone = article_container.clone();
                article_container_clone = update_heritage_data(article_container_clone, photo);
                selected_section.append(article_container_clone);
            count ++;
            // Finish preloader
            if (count == 5) {
                $('.preloader-wrapper').fadeOut();
            }
            });
        })
    }).catch(error => {
        console.log(error);
    });
};



// Update content when scroll down to the end
$(window).scroll(function () {
    if ($(window).scrollTop() + $(window).height() >= $(document).height()) {
        limit = 3;
        update_content($('.posts'), limit, {
            offset: offset
        });
        offset += limit;
    }

});

// Transparent nav bar when scroll the content.
window.addEventListener('scroll', function () {
    document.body.classList[
        window.scrollY > 20 ? 'add' : 'remove'
    ]('scrolled');
});

// Blur the content displayed in transparent navbar.
// ==================================================
var content = $('.content'),
    header = $('.header-float');

$(content).clone().prependTo(header).addClass('blurred');


$(document).scroll(function () {
    var scroll = $(this).scrollTop();
    $('.blurred').css({
        '-webkit-transform': 'translateY(-' + scroll + 'px)',
        'transform': 'translateY(-' + scroll + 'px)'
    });
})
// ====================================================

// Waypoint 19: Language Crowdsourcing
function getPrefferedLanguages() {
    var preffered_languages = navigator.languages;
    var result = [];
    preffered_languages.forEach(function(language){
        language = language.substr(0,2);
        if (result.indexOf(language) < 0) {
            result.push(language);
        }
    })
    return result
}

var $dropdown_content = $('.dropdown-content');
var preffered_languages = getPrefferedLanguages();
const abstract_dropdown_anchor = $('#anchor--abstract');

function updateDropdownOption(language) {
    var language_text = native_code[language];
    var anchor_clone = abstract_dropdown_anchor.clone();
    anchor_clone.text(language_text);
    anchor_clone.removeAttr('hidden').attr('id', language);
    $dropdown_content.append(anchor_clone);
}

preffered_languages.forEach(language => {
    updateDropdownOption(language);
})

function toggleDropdown(dropdown_button) {
    // not() Exception current element is selected
    $('.dropdown-content').not($(dropdown_button).siblings('.dropdown-content')).removeClass('show');
    $('.post-translate').not($(dropdown_button).find('.post-translate')).addClass('post-translate--shake');
    $(dropdown_button).siblings('.dropdown-content').toggleClass('show');    
    $(dropdown_button).find('.post-translate').toggleClass('post-translate--shake');
    $(dropdown_button).siblings('.dropdown-content').find('.language-input').focus();
}

// Set the value of language when choose a language 
function pickLanguage(language) {
    $(language).parent().attr('value', $(language).attr('id'));
    dropdown_button = $(language).parent().siblings('.post-btn');
    // toggleDropdown(dropdown_button);
    $(language).parent().siblings('.post-btn').find('.language_name').text(native_code[$(language).attr('id')]).show();
    $(language).parent().siblings('.post-btn').find('.post-translate').hide();
}

// Show the input field for caption
function showInput(language) {
    $(language).parents('.dropdown').siblings('.info__caption--text').hide();
    $(language).parents('.dropdown').siblings('.info__caption--input').show().focus();
}

const translate_src = './assets/img/translate.png';

function returnNormalState(caption_input) {
    $(caption_input).val('');
    $(caption_input).hide();
    $(caption_input).siblings('.info__caption--text').show();
    $(caption_input).siblings('.dropdown').find('.language_name').hide();
    $(caption_input).siblings('.dropdown').find('.dropdown-content').removeAttr('value');
    $(caption_input).siblings('.dropdown').find('.post-translate').show();
}

// Suggest the photo caption when the inputs are available
function suggestPhotoCaption(caption_input) {
    let caption_content = $(caption_input).val();
    let locale = alpha1_alpha3[$(caption_input).siblings('.dropdown').find('.dropdown-content').attr('value')];
    let photo_id = $(caption_input).parents('.post-container').attr('id');
    let dropdown_button = $(caption_input).siblings('.dropdown').find('.post-btn')
    if (!dropdown_button.is(":active")) {
        // toggleDropdown(dropdown_button);
        if (caption_content.length != 0) {
            mHeritageGoService.suggestPhotoCaption(photo_id, caption_content, locale)
                .catch(error => {
                    console.log(error);
                    alert('This feature is still under development. Please check back for updates.')
                });
        }
        returnNormalState(caption_input);    
    }
}


// Blur the input when press Enter
function suggestPhotoCaptionWithEnter(caption_input) {
    $(caption_input).on("keypress", function (e) {
        if (e.which == 13) {
            suggestPhotoCaption($(caption_input));
            $(caption_input).blur();
            
        }
    });
}

// Blur the input when scroll down
$(document).scroll(function () {
    if ($('.info__caption--input').is(":focus")) {
        $('.info__caption--input').blur();
    }
})

function filterFunction(input) {
    var filter_content = $(input).val();
    filter_content = filter_content.toUpperCase();
    dropdown_content = $(input).parent();
    language_options = dropdown_content.find('a');
    for (i = 1; i < language_options.length; i++) {
        txtValue = language_options[i].textContent || language_options[i].innerText;
        if (txtValue.toUpperCase().indexOf(filter_content) > -1) {
            language_options[i].style.display = "";
        } else {
            language_options[i].style.display = "none";
        }
    }
};

$(window).click(function(event){
    if (elements_contain_event.includes(event.target.className) == false) {
        if ($('.dropdown-content').hasClass('show')){
            $('.dropdown-content').removeClass('show');
            $('.post-translate').addClass('post-translate--shake');
        }
    }
});

// Like reaction for a Heritage
function likeReaction(reaction_like){
    if ($(reaction_like).find('.like--count').text() == '1'){
        $(reaction_like).find('.fa-heart').css({
            'color': 'black'
        });
        $(reaction_like).find('.like--count').html(0);    
    }
    else{
        $(reaction_like).find('.fa-heart').css({
            'color': '#F44747'
        });
        $(reaction_like).find('.like--count').html(1);
    }
}

