
export const bad_words_validator  =  (text)  => {
    // Validar que los camposr title y text no tengan malas palabras
    let bad_words = ['culo', 'puto el que lee', 'macri', 'chupito el pame']

    let list_bad_text = text.split(' ');

    let form_bad_words = []


    // for each word in list_title
    // || or
    // && and
    // ! not
    bad_words.forEach(bad_word => {
        if (list_bad_text.includes(bad_word) || list_bad_text.includes(bad_word)) {
        form_bad_words.push(bad_word)
        }
    })
    return form_bad_words
}
