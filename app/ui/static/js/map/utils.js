export {truncate_text}


let truncate_text = (text, max_length) => {
    if (text.length > max_length) {
        text = text.substr(0, max_length-3) + '...';
    }
    return text;
}