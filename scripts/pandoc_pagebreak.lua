-- Convert an explicit HTML page-break marker into a real Word page break.
function Div(element)
  if element.classes:includes('pagebreak') then
    return pandoc.RawBlock(
      'openxml',
      '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'
    )
  end
end
