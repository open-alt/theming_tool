// Copyright (c) 2020, Ahmed Al-Farran and contributors
// For license information, please see license.txt
var dirty = 0;
var site_name = "";
frappe.ui.form.on('Theme Settings', {
  // refresh: function(frm) {

  // }
  onload: function(frm){
    frappe.call({
      method: "theming_tool.theming_tool.doctype.theme_settings.theme_settings.get_site_name",
      callback: function(r) {
        site_name = r.message;
      }
    });
  },
  font: function(frm) {
    if (!frm.doc.font) {
      frm.doc.font_path = undefined;
      frm.refresh_fields("font_path");
      // $("body, h1, h2, h3, h4, h5, h6").css("font-family", "unset");
    }
  },
  before_save: function(frm) {
    var style = "";
    if (frm.is_dirty()) {
      dirty = 1;
    }
    if (frm.doc.font_path) {
      var file_name = frm.doc.font_path.substring(frm.doc.font_path.lastIndexOf('/') + 1);
      style = style + "@font-face {\nfont-family: CustomFont;\nsrc: url('/assets/" + site_name + "/theme/font/" + file_name + "') format('truetype');\n}\n";
      style = style + "body, h1, h2, h3, h4, h5, h6{\nfont-family: CustomFont !important;\n}\n"
    }
    if (frm.doc.logo){
      var image_name = frm.doc.logo.substring(frm.doc.logo.lastIndexOf('/') + 1);
      style = style + ".app-logo {\nwidth: 0px !important;\nheight: 0px !important;\npadding: 13px !important;\nbackground: url('/assets/" + site_name + "/theme/images/" + image_name + "');\nbackground-size: cover;\n}\n";
    }
    for (var i = 0; i < frm.doc.elements_colors.length; i++) {
      if (frm.doc.elements_colors.length > 0) {
        $(frm.doc.elements_colors[i].class).css("background-color", frm.doc.elements_colors[i].color);
        style = style + (frm.doc.elements_colors[i].class + " {\nbackground-color : " + frm.doc.elements_colors[i].color + "\n}\n");
      }
    }
    frm.doc.theme_scss = style;
    frm.refresh_fields("theme_scss");
  },
  after_save: function(frm) {
    if (dirty) {
      location.reload();
    }
  }
});
