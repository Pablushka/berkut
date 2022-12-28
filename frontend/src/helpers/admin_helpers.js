
export const bad_words_validator  =  (text)  => {
    // Validar que los camposr title y text no tengan malas palabras
    let bad_words = ['culo', 'puto el que lee', 'macri', 'chupito el pame']

    let list_bad_text = text.split(' ');

    let form_bad_words = []

    bad_words.forEach(bad_word => {
        form_bad_words = searchInText( bad_word, list_bad_text, form_bad_words)
    })

    // for each word in list_title
    // || or
    // && and
    // ! not

    // let response = []

    // if (form_bad_words.length > 0) {
    //     response = [form_bad_words, false]
    // } else {
    //     response = [ [], true]
    // }
    
    // return response
    
    let response = {}

    if (form_bad_words.length > 0) {
        response = {
            bad_words: form_bad_words,
            valid: false
        }
    } else {
        response = {
            bad_words: [],
            valid: true
        }
    }

    return response
}

const searchInText = (searchFor, content, result) => {
    if (content.includes(searchFor) || content.includes(searchFor)) {
        result.push(searchFor)
    }

    return result 
}
