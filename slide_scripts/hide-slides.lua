-- Pandoc Lua filter to conditionally hide slides based on tags/classes
-- Usage: pandoc input.md -t revealjs --lua-filter=hide-slides.lua -o output.html

-- Configuration: Set which tags/classes to hide
local HIDE_TAGS = {
  "optional",
  "hide",
  "appendix",
  "detailed"
}

-- Function to check if an element should be hidden
local function should_hide(elem)
  if elem.classes then
    for _, class in ipairs(elem.classes) do
      for _, hide_tag in ipairs(HIDE_TAGS) do
        if class == hide_tag then
          return true
        end
      end
    end
  end
  return false
end

-- Function to check metadata for hide flags
local function check_metadata()
  local meta = pandoc.Meta({})
  -- You can add metadata-based logic here if needed
  return meta
end

-- Filter for Div elements (slides wrapped in divs)
function Div(div)
  if should_hide(div) then
    return {}  -- Return empty, effectively removing the element
  end
  return div
end

-- Filter for Header elements (slide headers)
-- This works for reveal.js and other slide formats
function Header(header)
  if should_hide(header) then
    return {}  -- Remove the header
  end
  return header
end

-- Alternative: Filter based on horizontal rules (slide separators)
-- This is more complex and would require tracking state


