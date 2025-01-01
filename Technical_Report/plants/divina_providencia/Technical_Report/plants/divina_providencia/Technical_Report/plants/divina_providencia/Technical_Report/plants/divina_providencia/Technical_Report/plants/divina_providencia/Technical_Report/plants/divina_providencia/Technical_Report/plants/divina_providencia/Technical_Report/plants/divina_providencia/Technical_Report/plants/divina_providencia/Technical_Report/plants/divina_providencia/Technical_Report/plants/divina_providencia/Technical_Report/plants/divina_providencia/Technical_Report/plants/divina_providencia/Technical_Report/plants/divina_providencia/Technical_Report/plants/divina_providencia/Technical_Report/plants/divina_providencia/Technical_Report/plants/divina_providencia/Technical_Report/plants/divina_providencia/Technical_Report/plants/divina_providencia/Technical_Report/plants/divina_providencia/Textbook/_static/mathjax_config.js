// Dynamically load script then call helper when script has loaded.
function dynamicallyLoadScript(url, helper) {
    var script = document.createElement("script"); // Make a script DOM node
    script.src = url; // Set it's src to the provided URL

    document.head.appendChild(script); // Add it to the end of the head section of the page (could change 'head' to 'body' to add it to the end of the body section instead)
    script.onreadystatechange= function () {
      if (this.readyState == 'complete') helper();
     }
     script.onload= helper;
}

// Configure MathJax
function mathjax_config() {
  MathJax.Hub.Register.StartupHook("TeX Jax Ready",function () {
  MathJax.Hub.Insert(MathJax.InputJax.TeX.Definitions.macros,{
    cancel: ["Extension","cancel"],
    bcancel: ["Extension","cancel"],
    xcancel: ["Extension","cancel"],
    cancelto: ["Extension","cancel"]
    });
  });
}

var mathjax_url = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
dynamicallyLoadScript(mathjax_url, mathjax_config)
