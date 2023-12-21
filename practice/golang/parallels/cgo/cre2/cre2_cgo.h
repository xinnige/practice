#ifndef CRE2_CGO_H
#define CRE2_CGO_H

#ifdef __cplusplus
extern "C"
{
#endif

#include "cre2.h"

#ifndef CRE2_CGO_DECL
#define CRE2_CGO_DECL extern
#endif
    CRE2_CGO_DECL cre2_string_t * cre2_string_new(char *data, int length);
    CRE2_CGO_DECL void cre2_string_delete(cre2_string_t * s);
    CRE2_CGO_DECL bool match(cre2_regexp_t *rex, const char *text, int textlen);
    CRE2_CGO_DECL int global_replace(const char * pattern, cre2_string_t * text_and_target, cre2_string_t * rewrite);
    CRE2_CGO_DECL int global_replace_re	(cre2_regexp_t * rex,cre2_string_t * text_and_target, cre2_string_t * rewrite);
    CRE2_CGO_DECL int find_all_string_index(cre2_regexp_t *rex, const char *text, int textlen, int **match, int nmatch);
 
#ifdef __cplusplus
} // extern "C"
#endif

#endif