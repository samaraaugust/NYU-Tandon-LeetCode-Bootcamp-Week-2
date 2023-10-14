/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    let sec = {};
    let whether = true;
    if (s.length === t.length) {
        for (let i = 0; i < s.length; i++) {
            if (sec.hasOwnProperty(s[i])) {
                //is already accounted for
                if (t[i] === sec[s[i]]) {
                    continue;
                } else {
                    whether = false;
                    break;
                }
            } else {
                //is not matched 
                const values = Object.values(sec);
                if (values.includes(t[i])) {
                    //is already mapped
                    whether = false;
                    break;
                } else {
                    //not mapped so free
                    sec[s[i]] = t[i];
                }
            }
        }
    } else {
        whether = false;
    }
    return whether;
};
