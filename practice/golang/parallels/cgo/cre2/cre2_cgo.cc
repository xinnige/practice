#include <stdlib.h>

#include "cre2.h"
#include "cre2_cgo.h"


cre2_string_t * cre2_string_new(char *data, int length) { 
    cre2_string_t * s = (cre2_string_t *)malloc(sizeof(cre2_string_t));
    s->data = data;
    s->length = length;
    return s;
}

void cre2_string_delete(cre2_string_t * s) {
    delete s;
}

int global_replace(const char * pattern, cre2_string_t * text_and_target, cre2_string_t * rewrite) {
    return cre2_global_replace(pattern, text_and_target, rewrite);
}

int global_replace_re(cre2_regexp_t * rex, cre2_string_t * text_and_target, cre2_string_t * rewrite) {
    return cre2_global_replace_re( rex, text_and_target, rewrite);
}

bool match(cre2_regexp_t *rex, const char *text, int textlen){
    return cre2_match(rex, text, textlen, 0, textlen, CRE2_UNANCHORED, NULL, 0) == 1;
}

int find_all_string_index(cre2_regexp_t *rex, const char *text, int textlen, int **match, int nmatch)
{
    int cnt = 0;
    const char *start_addr = text;
    while (cnt < nmatch && textlen > 0)
    {
        cre2_string_t str;
        if (!cre2_match(rex, text, textlen, 0, textlen, CRE2_UNANCHORED, &str, 1))
        {
            return cnt;
        }
        ((int *)match + cnt * 2)[0] = str.data - start_addr;
        ((int *)match + cnt * 2)[1] = ((int *)match + cnt * 2)[0] + str.length;
        textlen -= str.data + str.length - text;
        text = str.data + str.length;
        cnt++;
    }
    return cnt;
}