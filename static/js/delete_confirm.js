/**
 * Created by Artem on 11/30/2016.
 */

// function addEvent(node, type, callback) {
//     if(node.addEventListener) {
//         node.addEventListener(type, function(e) {
//             return callback(e, e.target)
//         }, false)
//     }
//     else if(node.attachEvent) {
//         node.attachEvent('on' + type, function(e) {
//             return callback(e, e.srcElement)
//         }, false)
//     }
// }
//
// delete_forms = document.getElementsByName('delete_form');
// for (var i = 0; i < delete_forms.length; i++) {
//     addEvent(delete_forms[i], 'submit', function(e, target) {
//     c = confirm('Are you sure?');
//     if(!c) {
//         e.preventDefault();
//         return false;
//     }
//     else {
//         return true;
//     }
//     });
// }