/**
 * Created by Artem on 11/29/2016.
 */

var elements = [
    document.getElementsByTagName("input"),
    document.getElementsByTagName("textarea")
];

function addEvent(node, type, callback) {
    if(node.addEventListener) {
        node.addEventListener(type, function(e) {
            callback(e, e.target);
        }, false);
    }
    else if (node.attachEvent) {
        node.attachEvent('on' + type, function(e) {
            callback(e, e.srcElement);
        }, false);
    }
}


function getErrorMessage(field) {
    pattern = field.getAttribute("pattern");
    value = field.value;

    if (field.required && !value)
        return field.getAttribute("name")+" is required";
    if (!field.required && !value)
        return "";
    if (pattern && !(new RegExp(pattern).test(value)))
        return "Invalid format";

    return "";
}

var has_invalid = false;
for (var i = 0; i < elements.length; i++) {
    for (var j = 0; j < elements[i].length; j++)
        if(getErrorMessage(elements[i][j])) {
            has_invalid = true;
        }
    }
if(!has_invalid)
    document.getElementById("id_create_btn").removeAttribute("disabled")


function instantValidation(field) {
    error_msg = getErrorMessage(field);
    if(!error_msg) {
        field.parentElement.classList.remove("has-error");
        error = document.getElementById("id_"+field.getAttribute("name")+"_error");
        if(error) {
            error.parentNode.removeChild(error);
        }
    }
    else {
        error_element = document.getElementById("id_"+field.getAttribute("name")+"_error");
        if (!error_element) {
            var divBlock = document.createElement('span');
            divBlock.innerHTML = "<span>"+error_msg+"</span>";
            divBlock.className = "error text-danger";
            divBlock.id = "id_"+field.getAttribute("name")+"_error";
        }
        else {
            error_element.innerHTML = "<span>"+error_msg+"</span>";
        }

        field.parentElement.appendChild(divBlock);
        field.parentElement.classList.add("has-error");
        document.getElementById("id_create_btn").setAttribute("disabled", "disabled");
    }
    var has_invalid = false;
    for (var i = 0; i < elements.length; i++) {
        for (var j = 0; j < elements[i].length; j++)
            if(getErrorMessage(elements[i][j])) {
                has_invalid = true;
            }
        }
    if(!has_invalid)
        document.getElementById("id_create_btn").removeAttribute("disabled")
}


for (var i = 0; i < elements.length; i++) {
    for (var j = 0; j < elements[i].length; j++)
        addEvent(elements[i][j], 'input', function(e, target) {
            instantValidation(target);
        })
}