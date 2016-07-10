var gt = new Gettext({domain: 'flask-i18n-example'});
var _ = function(msgid) { return gt.gettext(msgid); };
var ngettext = function(msgid, msgid_plural, n) { return gt.ngettext(msgid, msgid_plural, n); };

var entries = [
    _("We're all sausages!"),
    gt.strargs(_("%1 is a bit like %2"), [_("Chouchen"), _("Mead")]),
    gt.strargs(ngettext("This document contains a tip", "This document contains %1 tips", 1), [1]),
    gt.strargs(ngettext("This document contains a tip", "This document contains %1 tips", 51), [51])
];

var fill_me = document.getElementById("fill_me");
for (entry in entries) {
    fill_me.appendChild(document.createTextNode(entries[entry]));
    fill_me.appendChild(document.createElement('br'));
    fill_me.appendChild(document.createElement('br'));
}
