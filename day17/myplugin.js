/**
 * Created by cq on 2017/11/5.
 */

status = 1;

$.extend({
   'ChangeMenu': function (nid) {
       var current_header = document.getElementById(nid);
            var item_list = current_header.parentElement.parentElement.children;
            for(var i=0;i<item_list.length;i++){
                var current_item = item_list[i];
                current_item.children[1].classList.add('hide');
            }
            current_header.nextElementSibling.classList.remove('hide');
   }
});
