# Cheat Sheek

**Cascading Style Sheets** 

(CSS 3)

![](_page_0_Picture_4.jpeg)

Powered by 🕌 HOSTINGER

![](_page_0_Picture_6.jpeg)

![](_page_0_Picture_7.jpeg)

| BACKGROUND        | 1 | PSUEDO-CLASS         | 9  |
|-------------------|---|----------------------|----|
| BORDER            | 1 | PSUEDO-ELEMENTS      | 9  |
| TABLE             | 1 | UI                   | 9  |
| BOX MODEL         | 2 |                      |    |
| TRANSITIONS       | 2 | UNITS                | 10 |
| COLOR             | 3 | ANGELS               | 10 |
| FONT              | 3 | ABSOLUTE MEASUREMENT | 10 |
| ANIMATIONS        | 4 | COLORS               | 10 |
| COLUMN            | 4 | FREQUENCY            | 10 |
| TEXT              | 4 | RELATIVE MEASUREMENT | 10 |
| SPEECH            | 5 | TIME                 | 10 |
| TEMPLATE LAYOUT   | 5 |                      |    |
| 3D / 2D TRANSFORM | 6 | SELECTOR TYPES       | 11 |
| GRID POSITIONING  | 6 |                      |    |
| HYPERLINK         | 6 |                      |    |
| LIST AND MARKERS  | 6 |                      |    |
| OUTLINE           | 6 |                      |    |
| GENERATED CONTENT | 7 |                      |    |
| POSITIONING       | 7 |                      |    |
| RUBY              | 7 |                      |    |
| LINE BOX          | 8 |                      |    |
| PAGED MEDIA       | 8 |                      |    |

### BACKGROUND

### BORDER

<span id="page-2-0"></span>

| background            | background-image background-position background-size background-repeat background-attachment background-origin background-clip background-color                   |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| background-attachment | scroll   fixed                                                                                                                                                    |
| background-break      | bounding-box   each-box  <br>continuous                                                                                                                           |
| background-clip       | length<br>%<br>border-box   padding-box  <br>content-box   no-clip                                                                                                |
| background-color      | color<br>transparent                                                                                                                                              |
| background-image      | <i>url</i><br>none                                                                                                                                                |
| background-origin     | border-box   padding-box  <br>content-box                                                                                                                         |
| background-position   | top left   top center   top<br>right   center left   center<br>center   center right  <br>bottom left   bottom center<br>  bottom right<br>x-% y-%<br>x-pos y-pos |
| background-repeat     | repeat   repeat-x   repeaty<br>  no-repeat                                                                                                                        |
| background-size       | length<br>%<br>auto   cover   contain                                                                                                                             |

### TABLE

| border-collapse | collapse   separate         |
|-----------------|-----------------------------|
| border-spacing  | length length               |
| caption-side    | top   bottom   left   right |
| empty-cells     | show   hide                 |
| table-layout    | table-layout auto   fixed   |

| border              | border-width                 |
|---------------------|------------------------------|
| border              | border-style                 |
|                     | border-style<br>border-color |
|                     |                              |
| border-break        | border-width                 |
|                     | border-style                 |
|                     | color                        |
|                     | close                        |
| border-bottom       | border-bottom-width          |
| border-bottom       | border-style                 |
|                     | border-style<br>border-color |
|                     | 501461-60101                 |
| border-bottom-color | border-color                 |
|                     |                              |
| border-bottom-style | border-style                 |
| border-bottom-width | thin   medium   thick        |
|                     | length                       |
|                     |                              |
| border-collapse     | collapse   separate          |
|                     |                              |
| border-color        | color                        |
| border-image        | image                        |
|                     | [ number / %                 |
|                     | border-width                 |
|                     | stretch   repeat   round ]   |
|                     | none                         |
|                     |                              |
| border-left         | border-left-width            |
|                     | border-style                 |
|                     | border-color                 |
| border-left-color   | border-color                 |
|                     |                              |
| border-left-style   | border-style                 |
|                     |                              |
| border-left-width   | thin   medium   thick        |
|                     | length                       |
| border-right        | border-right-width           |
| border-right        | border-style                 |
|                     | border-style<br>border-color |
|                     |                              |
| border-right-color  | border-color                 |
|                     |                              |
| border-right-style  | border-style                 |
| border-right-width  | thin   medium   thick        |
| 23 del light white  | length                       |
|                     |                              |
|                     |                              |

<span id="page-3-0"></span>

| border-top                 | border-top-width<br>border-style<br>border-color                                                             |
|----------------------------|--------------------------------------------------------------------------------------------------------------|
| border-top-color           | border-color                                                                                                 |
| border-top-style           | border-style                                                                                                 |
| border-top-width           | thin   medium   thick<br>length                                                                              |
| border-width               | thin   medium   thick<br>length                                                                              |
| border-radius              | border-top-right-radius<br>border-bottom-right-radius<br>border-bottom-left-radius<br>border-top-left-radius |
| border-top-right-radius    | length                                                                                                       |
| border-bottom-right-radius | length                                                                                                       |
| border-bottom-left-radius  | length                                                                                                       |
| border-top-left-radius     | length                                                                                                       |
| box-shadow                 | inset    [ length, length,<br>length, length    <color> ]<br/>none</color>                                   |
| border-style               | none   hidden   dotted  <br>dashed   solid   double  <br>groove   ridge   inset  <br>outset                  |

| transition                 | transition-property<br>transition-duration<br>transition-timing-function<br>transition-delay              |
|----------------------------|-----------------------------------------------------------------------------------------------------------|
| transition-delay           | time                                                                                                      |
| transition-duration        | time                                                                                                      |
| transition-property        | none   all                                                                                                |
| transition-timing-function | ease   linear   ease-in  <br>ease-out   ease-in-out  <br>cubic-Bezier (number,<br>number, number, number) |

| clear         | left   right   both   none                                                                                                                                                                                                                                                                                                      |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| display       | none   inline   block   inlineblock<br>  list-item   run-in  <br>compact   table   inlinetable<br>  table-row-group  <br>table-header-group   tablefooter<br>group   table-row  <br>table-column-group   tablecolumn<br>  table-cell   tablecaption<br>  ruby   ruby-base  <br>ruby-text   ruby-base-group<br>  ruby-text-group |
| float         | left   right   none                                                                                                                                                                                                                                                                                                             |
| height        | auto<br>length<br>%                                                                                                                                                                                                                                                                                                             |
| max-height    | none<br>length<br>%                                                                                                                                                                                                                                                                                                             |
| max-width     | none<br>length<br>%                                                                                                                                                                                                                                                                                                             |
| min-height    | none   inherit<br>length<br>%                                                                                                                                                                                                                                                                                                   |
| min-width     | none   inherit<br>length<br>%                                                                                                                                                                                                                                                                                                   |
| width         | auto<br>%<br>length                                                                                                                                                                                                                                                                                                             |
| margin        | margin margin-top<br>margin-right<br>margin-bottom<br>margin-left                                                                                                                                                                                                                                                               |
| margin-bottom | auto<br>length<br>%                                                                                                                                                                                                                                                                                                             |
| margin-left   | auto<br>length<br>%                                                                                                                                                                                                                                                                                                             |
| margin-right  | auto<br>length<br>%                                                                                                                                                                                                                                                                                                             |

BOX MODEL

FONT

<span id="page-4-0"></span>

| margin-top         | auto<br>Iength<br>%                                                                      |
|--------------------|------------------------------------------------------------------------------------------|
| padding            | padding padding-top<br>padding-right<br>padding-bottom<br>padding-left                   |
| padding-bottom     | length<br>%                                                                              |
| padding-left       | length<br>%                                                                              |
| padding-right      | length<br>%                                                                              |
| padding-top        | length<br>%                                                                              |
| marquee-direction  | forward   reverse                                                                        |
| marquee-loop       | infinite<br>number                                                                       |
| marquee-play-count | infinite<br>integer                                                                      |
| marquee-speed      | slow   normal   fast                                                                     |
| marquee-style      | scroll   slide   alternate                                                               |
| overflow           | visible   hidden   scroll  <br>auto   no-display   nocontent<br>overflow-x<br>overflow-y |
| overflow-style     | auto   marquee-line   marquee-<br>block                                                  |
| overflow-x         | visible   hidden   scroll  <br>auto   no-display   nocontent                             |
| overflow-y         | visible   hidden   scroll  <br>auto   no-display   nocontent                             |
| rotation           | angle                                                                                    |
| rotation-point     | position (paired value offset)                                                           |
| visibility         | visibility visible   hidden  <br>collapse                                                |

| font                       | font-style font-variant font-weight font-size/line-height font-family caption   icon   menu   message-box   smallcaption   status-bar |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| font-family                | family-name<br>generic-family<br>inherit                                                                                              |
| font-size                  | xx-small   x-small   small  <br>medium   large   x-large  <br>xx-large   smaller   larger  <br>inherit<br>length<br>%                 |
| font-size-adjust           | none  inherit<br>number                                                                                                               |
| font-stretch               | normal   wider   narrower  <br>ultra-condensed   extracondensed                                                                       |
|                            | condensed   semi-condensed<br>  semiexpanded   expanded  <br>extra-expanded   ultraexpanded<br>  inherit                              |
| font-style                 | semiexpanded   expanded   extra-expanded                                                                                              |
| font-style<br>font-variant | semiexpanded   expanded  \nextra-expanded   ultraexpanded   inherit  normal   italic   oblique                                        |
|                            | semiexpanded   expanded  \nextra-expanded   ultraexpanded   inherit  normal   italic   oblique  \ninherit                             |

### COLOR

| color   | inherit<br>color  |  |
|---------|-------------------|--|
| opacity | inherit<br>number |  |

<span id="page-5-0"></span>

| direction            | ltr   rtl   inherit                                                                       |  |
|----------------------|-------------------------------------------------------------------------------------------|--|
| hanging-punctuation  | none   [ start   end   endedge ]                                                          |  |
| letter-spacing       | normal<br>length<br>%                                                                     |  |
| punctuation-trim     | none   [start   end   adjacent]                                                           |  |
| text-align           | start   end   left   right  <br>center   justify                                          |  |
| text-align-last      | start   end   left   right  <br>center   justify                                          |  |
| text-decoration      | none   underline   overline  <br>line-through   blink                                     |  |
| text-emphasis        | none   [ [ accent   dot   circle<br>  disc] [ before   after ]? ]                         |  |
| text-indent          | length<br>%                                                                               |  |
| text-justify         | auto   inter-word   interideograph<br>  inter-cluster   distribute  <br>kashida   tibetan |  |
| text-outline         | none<br>color<br>length                                                                   |  |
| text-shadow          | none<br>color<br>length                                                                   |  |
| text-transform       | none   capitalize   uppercase<br>  lowercase                                              |  |
| text-wrap            | normal   unrestricted   none<br>  suppress                                                |  |
| unicode-bidi         | normal   embed   bidioverride                                                             |  |
| white-space          | normal   pre   nowrap   prewrap<br>  pre-line                                             |  |
| white-space-collapse | preserve   collapse   preserve<br>breaks   discard                                        |  |
| word-break           | normal   keep-all   loose  <br>break-strict   break-all                                   |  |
| word-spacing         | normal<br>length<br>%                                                                     |  |
| word-wrap            | normal   break-word                                                                       |  |

| column-count      | auto<br>number                                              |
|-------------------|-------------------------------------------------------------|
| column-fill       | auto   balance                                              |
| column-gap        | normal<br>length                                            |
| column-rule       | column-rule-width<br>column-rule-style<br>column-rule-color |
| column-rule-color | color                                                       |
| column-rule-style | border-style                                                |
| column-rule-width | thin   medium   thick<br>length                             |
| columns           | column-width<br>column-count                                |
| column-span       | 1   all                                                     |
| column-width      | auto<br>length                                              |

| animation                 | animation-name<br>animation-duration<br>animation-timing-function<br>animation-delay<br>animation-iteration-count<br>animation-direction |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| animation-delay           | time                                                                                                                                     |
| animation-direction       | normal   alternate                                                                                                                       |
| animation-duration        | time                                                                                                                                     |
| animation-iteration-count | inherit<br>number                                                                                                                        |
| animation-name            | none   IDENT                                                                                                                             |
| animation-play-state      | running   paused                                                                                                                         |
| animation-timing-function | ease   linear   ease-in  <br>ease-out   ease-in-out  <br>cubic-Bezier (number,<br>number, number, number)                                |

SPEECH

### SPEECH

<span id="page-6-0"></span>

| cue             | cue-before                                                                                     |
|-----------------|------------------------------------------------------------------------------------------------|
| - Cuc           | cue-after                                                                                      |
| cue-before      | <pre>uri [ silent   x-soft   soft   medium   loud   x-loud]   none   inherit ] number %</pre>  |
| cue-after       | uri [ silent   x-soft   soft  <br>medium   loud   x-loud]  <br>none   inherit ]<br>number<br>% |
| mark            | mark-before<br>mark-after                                                                      |
| mark-before     | string                                                                                         |
| mark-after      | string                                                                                         |
| pause           | pause-before<br>pause-after                                                                    |
| pause-before    | none   x-weak   weak  <br>medium   strong   x-strong<br>  inherit<br>time                      |
| pause-after     | none   x-weak   weak  <br>medium   strong   x-strong<br>  inherit<br>time                      |
| phonemes string | string                                                                                         |
| rest            | rest-before<br>rest-after                                                                      |
| rest-before     | none   x-weak   weak  <br>medium   strong   x-strong<br>  inherit<br>time                      |
| rest-after      | none   x-weak   weak  <br>medium   strong   x-strong<br>  inherit<br>time                      |
| speak           | none   normal   spell-out  <br>digits   literal-punctuation  <br>no-punctuation   inherit      |
| voice-balance   | left   center   right   leftwards<br>  rightwards   inherit<br>number                          |
| voice-duration  | time                                                                                           |

| voice-family      | inherit   [ <specific-voice,<br>age, generic-voice, number&gt; ]</specific-voice,<br> |
|-------------------|---------------------------------------------------------------------------------------|
| voice-rate        | x-slow   slow   medium  <br>fast   x-fast   inherit<br>%                              |
| voice-pitch       | x-low   low   medium   high<br>  x-high   inherit<br>number<br>%                      |
| voice-pitch-range | x-low   low   medium   high<br>  x-high   inherit<br>number                           |
| voice-stress      | strong   moderate   none  <br>reduced   inherit                                       |
| voice-volume      | silent   x-soft   soft   medium<br>  loud   x-loud   inherit<br>number<br>%           |

### TEMPLATE LAYOUT

| box-align      | start   end   center   base                            |
|----------------|--------------------------------------------------------|
| box-direction  | normal   reverse                                       |
| box-flex       | number                                                 |
| box-flex-group | integer                                                |
| box-lines      | single   multiple                                      |
| box-orient     | horizontal   vertical   inlineaxis<br>  block-axis     |
| box-pack       | start   end   center   justify                         |
| box-sizing     | content-box   padding-box  <br>border-box   margin-box |
| tab-side       | top   bottom   left   right                            |

### LIST & MARKERS

<span id="page-7-0"></span>

| list-style          | list-style-type<br>list-style-position<br>list-style-image                                                                                                                                                                                                                                                                          |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| list-style-image    | none<br>url                                                                                                                                                                                                                                                                                                                         |
| list-style-position | Inside   outside                                                                                                                                                                                                                                                                                                                    |
| list-style-type     | none   asterisks   box   check   circle   diamond   disc   hyphen   square   decimal   decimal-leadingzero   lower-roman   upperroman   lower-alpha   upper- alpha   lower-greek   lower-latin   upper-latin   hebrew   armenian   georgian   cjk-ideographic   hiragana   katakana   hiragana-\niroha   katakana-iroha   footnotes |
| marker-offset       | auto<br>length                                                                                                                                                                                                                                                                                                                      |

### **GRID POSITIONING**

| grid-columns | none   inherit<br>[ length percentage relative<br>length ] |
|--------------|------------------------------------------------------------|
| grid-rows    | none   inherit<br>[ length percentage relative<br>length ] |

### OUTLINE

| outline        | outline-color<br>outline-style<br>outline-width                                 |
|----------------|---------------------------------------------------------------------------------|
| outline-color  | color<br>invert                                                                 |
| outline-offset | inherit<br>Iength                                                               |
| outline-style  | None   dotted   dashed  <br>solid   double   groove  <br>ridge   inset   outset |
| outline-width  | thin   medium   thick<br>length                                                 |

### 3D / 2D TRANSFORM

| backface-visibility | visible   hidden                                                                                                                                                                                                                                                         |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| perspective         | none<br>number                                                                                                                                                                                                                                                           |
| perspective-origin  | <pre>[[[ percentage&gt;   <length>   left   center   right ][   <percentage>   <length>   top      center   bottom ]? ] <length> ]      [[ left   center   right ]       [ top   center   bottom ]]    <length> ]</length></length></length></percentage></length></pre> |
| transform           | none   matrix   matrix3d   translate3d   translateX   translateY   translateZ   scale   scale3d   scaleX   scaleY   scaleZ   rotate   rotate3d   rotateX   rotateY   rotateZ   skewX   skewY   skew   perspective                                                        |
| transform-origin    | <pre>[[[ &lt; percentage&gt;  </pre>                                                                                                                                                                                                                                     |
| transform-style     | flat   preserve-3d                                                                                                                                                                                                                                                       |

### HYPERLINK

| target          | target-name<br>target-new<br>target-position       |
|-----------------|----------------------------------------------------|
| target-name     | current   root   parent   new<br>  modal<br>string |
| target-new      | window   tab   none                                |
| target-position | above   behind   front  <br>back                   |

## GENERATED CONTENT

<span id="page-8-0"></span>

| bookmark-label      | content attr string            |
|---------------------|--------------------------------|
| bookmark-level      | none<br>integer                |
| bookmark-target     | self<br>uri<br>attr            |
| border-length       | auto<br>length                 |
| content             | normal   none   inhibit<br>uri |
| counter-increment   | none<br>identifier number      |
| counter-reset       | none<br>identifier number      |
| crop                | auto<br>shape                  |
| display             | normal   none   list-item      |
| float-offset        | length length                  |
| hyphenate-after     | auto<br>integer                |
| hyphenate-before    | auto<br>integer                |
| hyphenate-character | auto<br>integer                |
| hyphenate-lines     | no-limit<br>integer            |
| hyphenate-resource  | none<br>uri                    |
| hyphens             | none   manual   auto           |
| image-resolution    | normal   auto<br>dpi           |
| marks               | [ crop    cross ]   none       |
| move-to             | normal   here<br>identifier    |
| page-policy         | start   first   last           |
| quotes              | none<br>string string string   |

## GENERATED CONTENT

| string-set   | identifier<br>content-list                      |
|--------------|-------------------------------------------------|
| text-replace | none<br>[ <string> <string>]+</string></string> |

### **POSITIONING**

| bottom   | auto<br>%<br>length                  |
|----------|--------------------------------------|
| clip     | shape<br>auto                        |
| left     | auto<br>%<br>length                  |
| position | static   relative   absolute   fixed |
| right    | auto<br>%<br>length                  |
| top      | auto<br>%<br>length                  |
| z-index  | auto<br>number                       |

### RUBY

| ruby-align    | auto   start   left   center  <br>end   right   distribute-letter<br>  distribute-space   lineedge |
|---------------|----------------------------------------------------------------------------------------------------|
| ruby-overhang | auto   start   end   none                                                                          |
| ruby-position | before   after   right   inline                                                                    |
| ruby-span     | attr(x)   none                                                                                     |

### LINE BOX

<span id="page-9-0"></span>

| alignment-adjust           | auto   baseline   beforeedge<br>  text-before-edge  <br>middle   central   after-edge<br>  text-after-edge   ideographic<br>  alphabetic   hanging<br>  mathematical<br>  length |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| alignment-baseline         | baseline   use-script   before-<br>edge   text-beforeedge<br>  after-edge   textafter-<br>edge   central   middle<br>  ideographic   alphabetic  <br>hanging   mathematical      |
| baseline-shift             | baseline   sub   super<br>length<br>%                                                                                                                                            |
| dominant-baseline          | auto   use-script   nochange<br>  reset-size   alphabetic<br>  hanging   ideographic<br>  mathematical  <br>central   middle   text-after-<br>edge   text-before-edge            |
| drop-initial-after-align   | alignment-baseline                                                                                                                                                               |
| drop-initial-after-adjust  | central   middle   after-edge<br>  text-after-edge   ideographic<br>  alphabetic  <br>mathematical<br>length<br>%                                                                |
| drop-initial-before-align  | caps-height<br>alignment-baseline                                                                                                                                                |
| drop-initial-before-adjust | before-edge   text-beforeedge<br>  central   middle  <br>hanging   mathematical<br>length<br>%                                                                                   |
| drop-initial-value         | initial<br>integer                                                                                                                                                               |
| drop-initial-size          | auto<br>integer<br>%<br>line                                                                                                                                                     |
| inline-box-align           | initial   last<br>integer                                                                                                                                                        |
| line-height                | normal number length                                                                                                                                                             |

### LINE BOX

| line-stacking          | line-stacking-strategy<br>line-stacking-ruby<br>line-stacking-shift                            |
|------------------------|------------------------------------------------------------------------------------------------|
| line-stacking-strategy | inline-line-height   blockline-<br>height   max-height  <br>grid-height                        |
| line-stacking-ruby     | exclude-ruby   include-ruby                                                                    |
| line-stacking-shift    | consider-shifts   disregardshifts                                                              |
| text-height            | auto   font-size   text-size  <br>max-size                                                     |
| vertical-align         | Baseline   sub   super   top<br>  text-top   middle   bottom<br>  text-bottom<br>  length<br>% |

### PAGED MEDIA

| fit               | fill   hidden   meet   slice                                           |
|-------------------|------------------------------------------------------------------------|
| fit-position      | [top   center   bottom]   <br>[left   center   right]<br> length<br> % |
| image-orientation | auto<br>angle                                                          |
| orphans           | integer                                                                |
| page              | auto<br>identifier                                                     |
| page-break-after  | auto   always   avoid   left  <br>right                                |
| page-break-before | auto   always   avoid   left  <br>right                                |
| page-break-inside | auto   avoid                                                           |
| size              | auto   landscape   portrait<br>length                                  |
| windows           | integer                                                                |

<span id="page-10-0"></span>

| appearance | normal   inherit   [icon   window   desktop   workspace   document   tooltip   dialog   button   pushbutton   hyperlink   radiobutton   checkbox   menuitem   tab   menu   menubar   pull-down-menu   pop-up-menu   list-menu   radio-group   checkboxgroup   outline-tree   range   field   combo-box   signature   password] |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cursor     | auto   crosshair   default   pointer<br>  move   e-resize   ne-resize  <br>nw-resize   nresize   se-resize  <br>sw-resize   s-resize   w-resize  <br>text   wait   help<br>url                                                                                                                                                 |
| icon       | auto   inherit<br>url                                                                                                                                                                                                                                                                                                          |
| nav-index  | auto   inherit<br>number                                                                                                                                                                                                                                                                                                       |
| nav-up     | auto   inherit<br><id> [ current   root  <br/><target-name> ]</target-name></id>                                                                                                                                                                                                                                               |
| nav-right  | auto   inherit<br><id> [ current   root  <br/><target-name> ]</target-name></id>                                                                                                                                                                                                                                               |
| nav-down   | auto   inherit<br><id> [ current   root  <br/><target-name> ]</target-name></id>                                                                                                                                                                                                                                               |
| nav-left   | auto   inherit<br><id> [ current   root  <br/><target-name> ]</target-name></id>                                                                                                                                                                                                                                               |
| resize     | none   both   horizontal  <br>vertical   inherit                                                                                                                                                                                                                                                                               |

### PSEUDO-ELEMENT

| ::first-letter | Adds special style to the first letter of a text |
|----------------|--------------------------------------------------|
| ::first-line   | Adds special style to the first line of a text   |
| ::before       | Inserts some content before an element           |
| ::after        | Inserts some content after an element            |

| :active              | an activated element                                                           |
|----------------------|--------------------------------------------------------------------------------|
| :focus               | an element while the element<br>has focus                                      |
| :visited             | a visited link                                                                 |
| :hover               | an element when you mouse over it                                              |
| :link                | an unvisited link                                                              |
| :disabled            | an element while the element is disabled                                       |
| :enabled             | an element while the element is enabled                                        |
| :checked             | an element (form element control)<br>that is checked                           |
| :selection           | an element that is currently selected of highlighted by the user               |
| :lang                | Allows the author to specify a language to use in a specified element          |
| :nth-child(n)        | an element that is the n-th sibling                                            |
| :nth-last-child(n)   | an element that is the n-th sibling counting from the last sibling             |
| :first-child         | an element that is the first sibling                                           |
| :last-child          | an element that is the last sibling                                            |
| :only-child          | an element that is the only child                                              |
| :nth-of-type(n)      | an element that is the n-th sibling of its type.                               |
| :nth-last-of-type(n) | an element that is the n-th sibling of its type counting from the last sibling |
| :last-of-type        | an element that is the first sibling of its type                               |
| :first-of-type       | an element that is the last sibling of its type                                |
| :only-of-type        | an element that is the only child of that type                                 |
| :empty               | an element that has no children                                                |
| :root                | root element within the document                                               |
| :not(x)              | an element not represented<br>by the argument 'x'                              |
| :target              | a target element as specified<br>by a target in a URI                          |
|                      |                                                                                |

### ABSOLUTE MEASUREMENT

<span id="page-11-0"></span>

| %  | percentage              |
|----|-------------------------|
| cm | centimeter              |
| in | inch                    |
| mm | millimeter              |
| рс | pica (1p = 12 points)   |
| pt | point (1pt = 1/72 inch) |

### RELATIVE MEASUREMENT

| ch  | width of the "0" glyph found in<br>the font for the font size used to<br>render |
|-----|---------------------------------------------------------------------------------|
| em  | 1em = current font size of current element                                      |
| ex  | x-height of the element's font                                                  |
| gd  | the grid defined by 'layout-grid'                                               |
| рх  | pixel of the viewing device                                                     |
| rem | the font size of the root element                                               |
| vh  | the viewport's height                                                           |
| vw  | the viewport's width                                                            |
| vm  | viewport's height or width,<br>whichever is smaller of the two                  |

### **ANGLES**

| deg  | degrees |
|------|---------|
| grad | grads   |
| rad  | radians |
| turn | turns   |

### FREQUENCY

| Hz  | hertz      |
|-----|------------|
| kHz | kilo-hertz |

### TIME

| ms | milli-seconds |
|----|---------------|
| s  | seconds       |

### COLORS

| color name                                 | red, blue, green, dark green                                                                                     |  |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------|--|
| rgb(x,y,z)                                 | red = rgb(255,0,0)                                                                                               |  |
| rgb(x%,y%,z%)                              | red = rgb(100%,0,0)                                                                                              |  |
| rgba(x,y,z, alpha)                         | red = rgba(255,0,0)                                                                                              |  |
| #rrggbb                                    | red = #ff0000 (or shorthand =<br>#f00)                                                                           |  |
| hsl(hue, saturation,<br>lightness)         | red = hsl(0, 100%, 50%)                                                                                          |  |
| hsla(hue, saturation,<br>lightness, alpha) | red = hsl(0, 100%, 50%)                                                                                          |  |
| flavor                                     | An accent color (typically chosen<br>by the user) to customize the<br>user interface of the user agent<br>itself |  |
| currentColor                               | computed value of the 'currentColor' keyword is the computed value of the 'color' property                       |  |

<span id="page-12-0"></span>

| Universal           | Any element                                                                                                     | * { font: 10px Arial; }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|---------------------|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type                | Any element of that type                                                                                        | h1 { text-decoration:<br>underline; }                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Grouping            | Multiple elements of different types                                                                            | h1, h2, h3 { font-family: Verdana; }                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Class               | Multiple elements of different types<br>when you don't want to affect all<br>instances of that type             | .sampleclass { textdecoration:<br>underline; }                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Id                  | A single element type when you don't<br>want to affect all instances of that type                               | #sampleid { textdecoration:<br>underline; }                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Descendant          | An element that is below (in the<br>document tree) another element—no<br>matter how many levels below           | #gallery h1 { textdecoration:<br>underline; }                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Child               | An element that is directly below<br>(in the document tree) another element                                     | #title > p { font-weight: bold; }                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Adjacent<br>Sibling | All elements that share the same parent<br>and elements are in the same immediate<br>sequence                   | h1 + p { font-style: italic; }                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| General<br>Sibling  | All elements that share the same parent<br>and elements are in the same sequence<br>(not necessarily immediate) | h1 ~ p { font-style: italic; }                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Attribute           | An element with that matches<br>the attribute listed                                                            | E[selected] - att whatever the value<br>E[att="val"] - att with a specific value<br>E[rel~="next"] - att with a value is<br>a whitespace separated list<br>*[lang ="en"] - att value either<br>being exactly "val" or beginning<br>with "val" immediately followed<br>by "-"<br>E[att^="val"] - att value that<br>begins with the prefix "val"<br>E[att\$="val"] - att value that end<br>with the suffix "val"<br>E[att*="val"] - att value<br>contains at least one instance<br>of the substring "val" |