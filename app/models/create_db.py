from .base_model import db
from .shared_models import *
from argon2 import PasswordHasher

def create_db():
    create_users()
    create_category()
    create_subcategory()
    create_items()

def create_users():
    usr = user_info('adminaccount@email.com', 'admin', True)
    db.session.add(usr)
    get_userinfo = user_info.query.filter_by(email='adminaccount@email.com').first()
    ph = PasswordHasher()
    hash_password = ph.hash('adminpassw0rd')
    auth = user_auth(get_userinfo.id, get_userinfo.email, hash_password)
    db.session.add(auth)
    
    usr = user_info('useraccount@email.com', 'Test User1', False)
    db.session.add(usr)
    get_userinfo = user_info.query.filter_by(email='useraccount@email.com').first()
    ph = PasswordHasher()
    hash_password = ph.hash('us3rpassword')
    auth = user_auth(get_userinfo.id, get_userinfo.email, hash_password)
    db.session.add(auth)

    usr = user_info('useraccount2@email.com', 'Test User2', False)
    db.session.add(usr)
    get_userinfo = user_info.query.filter_by(email='useraccount2@email.com').first()
    ph = PasswordHasher()
    hash_password = ph.hash('passw0rduser')
    auth = user_auth(get_userinfo.id, get_userinfo.email, hash_password)
    db.session.add(auth)


    db.session.commit()

def create_items():
    # Items for Living Room
    item = item_info('Maimz Sofa', "The Maimz sofa is mid-century revival done to perfection. Linear and minimalistic, the beautifully edited profile has all the retro elements you love, like sheltering arms, bolster pillows and tapered splayed legs. So casually cool, the caramel faux leather upholstery brings the look right into the present."
                     , 799.99, "maimz_sofa.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Maimz Sofa').first()
    itemtag = item_tag(getitemid.item_id, 1)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 1)
    db.session.add(itemsubtag)

    item = item_info('Altari Sofa', "If style is the question, then the Altari sofa is the answer. Sporting clean lines and sleek track arms, the decidedly contemporary profile is enhanced with plump cushioning and a chenille-feel upholstery, so pleasing to the touch. Sure to play well with so many color schemes, this sofa in slate gray includes a pair of understated floral pattern pillows for fashionably fresh appeal."
                     , 499.99, "maimz_sofa.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Altari Sofa').first()
    itemtag = item_tag(getitemid.item_id, 1)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 1)
    db.session.add(itemsubtag)

    item = item_info('Miravel Sofa', "Marvel at the beauty of a subtle showstopper. The Miravel sofa appeals to those with a uniquely chic eye for comfort pieces. Its personality is one of playful simplicity, with curving, tapered arms incorporating movement into the structured silhouette. Whether in casual, contemporary or eclectic spaces, this sofa’s on-trend styling makes an impression."
                     , 399.00, "maimz_sofa.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Miravel Sofa').first()
    itemtag = item_tag(getitemid.item_id, 1)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 1)
    db.session.add(itemsubtag)

    item = item_info('Darcy Sofa', "Talk about fine lines and great curves. That’s the beauty of the Darcy sofa—made to suit your appreciation for clean, contemporary style. A striking flared frame, comfy pillow top armrests and an ultra-soft upholstery that holds up to everyday living complete this fashion statement."
                     , 399.99, "maimz_sofa.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Darcy Sofa').first()
    itemtag = item_tag(getitemid.item_id, 1)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 1)
    db.session.add(itemsubtag)


    item = item_info('Next-Gen DuraPella Performance Fabric Dual Power Reclining Sofa', """This sleek, ultra-modern power reclining sofa has it all. With designer looks and head-to-toe comfort, the Next-Gen DuraPella reclining sofa with drop-down table has the upscale look of leather at a scaled-down faux leather price. Its two-tone upholstery is more durable and water-repellent than regular leather, an added bonus for families with children or pets. Features including wireless and USB charging, an adjustable headrest and an extended "zero-gravity" ottoman for improved circulation make this the next generation of power recliners."""
                     , 1999.99, "durapella_performance_fabric_dual_power_recliner.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Next-Gen DuraPella Performance Fabric Dual Power Reclining Sofa').first()
    itemtag = item_tag(getitemid.item_id, 1)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 2)
    db.session.add(itemsubtag)

    item = item_info('Stoneland Manual Reclining Sofa', "For those that love the cool look of leather but long for the warm feel of fabric, the Stoneland reclining sofa delivers both with ease. Its high-performance padded faux leather is remarkably durable and easy to clean, just the thing for family spaces. Channel-stitched back cushions provide indulgent lumbar support for maximum comfort—not to mention fashion-forward flair."
                     , 899.99, "stoneland_manual_recliner.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Stoneland Manual Reclining Sofa').first()
    itemtag = item_tag(getitemid.item_id, 1)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 2)
    db.session.add(itemsubtag)

    item = item_info('Biscoe Performance Fabric Dual Power Reclining Sofa', "If style is the question, then the Biscoe power reclining sofa is the answer. Its clean-lined profile is beautifully contemporary. High-performance fabric and plump cushioning make it so easy to comfortably kick up your heels. The adjustable Easy View™ headrest allows a primo view of the TV, and the extended ottoman provides extra room to really stretch out. Simply sit back, chill out and recline away—this sofa is designed to be your favorite seat in the house."
                     , 1299.99, "biscoe_performance_fabric_dual_power_recliner.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Biscoe Performance Fabric Dual Power Reclining Sofa').first()
    itemtag = item_tag(getitemid.item_id, 1)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 2)
    db.session.add(itemsubtag)

    item = item_info('Mindanao Dual Power Leather Reclining Sofa', "If sleek and modern is your style, the Mindanao power reclining sofa is ready to deliver a fresh look in comfort seating. With a plethora of power features and perfectly positioned scoop seating for unparalleled relaxation, this recliner will be your go-to spot for watching TV, reading or just drifting off to sleep."
                     , 1499.99, "mindanao_dual_power_leather_recliner.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Mindanao Dual Power Leather Reclining Sofa').first()
    itemtag = item_tag(getitemid.item_id, 1)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 2)
    db.session.add(itemsubtag)


    item = item_info('Puckman Leather Accent Chair', "The Puckman accent chair has an ultra-modern vibe and indulgent feel. Its metal frame is a chic complement to brown leather seating. With its bronze-tone finish and urban industrial style, this accent chair impresses with high-end looks priced to entice."
                     , 389.99, "puckman_leather_accent_chair.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Puckman Leather Accent Chair').first()
    itemtag = item_tag(getitemid.item_id, 1)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 3)
    db.session.add(itemsubtag)

    item = item_info('Alesandra Oversized Chair', "Decidedly modern with a sense of relaxed ease, the Alesandra oversized chair looks at home in so many different places and spaces. Providing a highly distinctive look: substantial track arms with curved cornering, wrapped t-cushioning and low-to-the-floor block feet in a warm wood-tone finish. Sporting a subtle chevron texture, the parchment-tone upholstery takes neutral to new heights."
                     , 699.99, "alesandra_oversized_chair.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Alesandra Oversized Chair').first()
    itemtag = item_tag(getitemid.item_id, 1)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 3)
    db.session.add(itemsubtag)


    item = item_info('Cariton Coffee Table', "Oversized yet far from overdone, the Cariton coffee table masters the art of simplicity. Bold, blocky profile is enriched with plank-effect styling and a textured grayish brown finish for a look that’s cool and contemporary and a vibe that’s warm and inviting. Its generous scale makes it a natural complement for spacious sectionals."
                     , 259.99, "cariton_coffee_table.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Cariton Coffee Table').first()
    itemtag = item_tag(getitemid.item_id, 1)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 4)
    db.session.add(itemsubtag)

    item = item_info('Realyn Coffee Table', "Elevating the art of traditional cottage styling, the Realyn oval coffee table is sure to serve you beautifully for years to come. Antiqued two-tone aesthetic blends a chipped white with a distressed wood finished top for added charm. Classic cabriole legs and shapely lower shelf are a lovely twist. Decorative corbels add refinement."
                     , 339.99, "realyn_coffee_table.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Realyn Coffee Table').first()
    itemtag = item_tag(getitemid.item_id, 1)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 4)
    db.session.add(itemsubtag)


    item = item_info('Havalance 4-Piece Entertainment Center with 67'' TV Stand', "Set your sights on modern farmhouse style with the Havalance entertainment center. Distressed two-tone treatment blends a weathered gray with vintage white for an utterly charming effect. Turned posts lend a hearty, substantial look that feels right at home, while plenty of open shelving makes the aesthetic anything but heavy."
                     , 1549.97, "havalance_4p_entertainment_center_with_67TV_stand.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Havalance 4-Piece Entertainment Center with 67'' TV Stand').first()
    itemtag = item_tag(getitemid.item_id, 1)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 5)
    db.session.add(itemsubtag)

    item = item_info('Yarlow 70" TV Stand', "Set your sights on modern farmhouse style with the Havalance entertainment center. Distressed two-tone treatment blends a weathered gray with vintage white for an utterly charming effect. Turned posts lend a hearty, substantial look that feels right at home, while plenty of open shelving makes the aesthetic anything but heavy."
                     , 269.99, "yarlow_70_TV_stand.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Yarlow 70" TV Stand').first()
    itemtag = item_tag(getitemid.item_id, 1)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 5)
    db.session.add(itemsubtag)


    # Items for Bedroom
    item = item_info('Foyland Queen Panel Storage Bed', "The Foyland panel storage bed is casual style simply done right. Its two-tone color scheme and picture frame headboard provide just the right touch of contemporary charm. Two deep storage drawers generously accommodate your wardrobe needs with ease."
                     , 999.99, "foyland_queen_panel_storage_bed.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Foyland Queen Panel Storage Bed').first()
    itemtag = item_tag(getitemid.item_id, 2)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 7)
    db.session.add(itemsubtag)

    item = item_info('Willowton King Panel Bed', "The ultimate look for a beach cottage or shabby chic inspired retreat, the Willowton king panel bed carries you away to a dreamy time and place. Its driftwoody whitewash finish is wonderfully easy on the eyes. Faux plank detailing incorporates a classically rustic touch that's so homey and comforting. Mattress and foundation/box spring sold separately."
                     , 599.99, "willowton_king_panel_bed.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Willowton King Panel Bed').first()
    itemtag = item_tag(getitemid.item_id, 2)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 7)
    db.session.add(itemsubtag)


    item = item_info('Lexann Twin Comforter Set', "Bring a sophisticated look to your bedroom with the Lexann comforter set. Featuring a solid pink background with a stitched diamond design, this comforter reverses to a crisp and fresh arrow design in pink, white and gray—giving you the choice to change up your bedroom decor quickly and easily."
                     , 59.99, "lexann_twin_comforter_set.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Lexann Twin Comforter Set').first()
    itemtag = item_tag(getitemid.item_id, 2)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 8)
    db.session.add(itemsubtag)

    item = item_info('Adason King Comforter Set', "Contemporary cool from head to toe. The Adason king comforter set provides a pop of pattern in blue and white for your restful retreat, recalling tile motifs. It reverses to a solid blue for ultimate versatility when it comes to relaxing in refinement."
                     , 109.99, "adason_king_comforter_set.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Adason King Comforter Set').first()
    itemtag = item_tag(getitemid.item_id, 2)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 8)
    db.session.add(itemsubtag)


    item = item_info('Robbinsdale 7 Drawer Dresser and Mirror', "Elegant, timeless furnishings take your bedroom to the next level. Nothing does that better than the Robbinsdale dresser with mirror. The antiqued white finish with a wonderful grain texture radiates sophistication, while the dark bronze-tone hardware adds an ornate touch. A hidden pull-out tray behind the top middle drawer puts your small valuables out of sight. Felt-finished top drawers round out the piece for the ultimate tasteful bedroom."
                     , 899.99, "robbinsdale_7_drawer_dresser_and_mirror.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Robbinsdale 7 Drawer Dresser and Mirror').first()
    itemtag = item_tag(getitemid.item_id, 2)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 9)
    db.session.add(itemsubtag)

    item = item_info('Finch 6 Drawer Dresser', "Practical and attractive, the Finch dresser blends seamlessly with modern decor and makes a smart addition to a bedroom. The six full-sized drawers slide easily and can be used to keep your clothes neat and organized. Sleek metal pulls in a brushed nickel-tone finish add to the streamlined aesthetic. Combine with other pieces in the collection to create a room that’s smart and stylish."
                     , 199.99, "finch_6_drawer_dresser.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Finch 6 Drawer Dresser').first()
    itemtag = item_tag(getitemid.item_id, 2)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 9)
    db.session.add(itemsubtag)


    item = item_info('Shawburn 20" 1 Drawer Nightstand', "Give provincial a new meaning with the chic look of the Shawburn nightstand. A two-tone finish keeps this piece light and fresh, while the warm pewter-tone hardware adds an industrial touch. The open cubby provides display space or accommodates a storage bin to add a delightfully homespun charm to your space."
                     , 59.99, "finch_6_drawer_dresser.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Shawburn 20" 1 Drawer Nightstand').first()
    itemtag = item_tag(getitemid.item_id, 2)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 10)
    db.session.add(itemsubtag)

    item = item_info('Danziar 22" 2 Drawer Charging Nightstand', "Sophisticated style for the savvy shopper. The Danziar nightstand prioritizes affordable, on-trend design. Its subtle replicated texture recalls the natural beauty of wood, highlighting the clean-lined form. And a matte black finish savvily suits different approaches to modern aesthetics. Mix and match with light and bright hues, or pair with other dark tones for a moody look."
                     , 249.99, "danziar_22_2_drawer_charging_nightstand.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Danziar 22" 2 Drawer Charging Nightstand').first()
    itemtag = item_tag(getitemid.item_id, 2)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 10)
    db.session.add(itemsubtag)


    item = item_info('Tartonelle Accent Chair', "Fresh and sophisticated. The Tartonelle accent chair with button tufting is a classy addition to your home. Inside-out design with linen weave fabric on the seating area and taupe faux leather on the back. Large nailhead trim ties the look together. Charles of London arms and turned bun feet make this a stylish heirloom piece."
                     , 359.99, "tartonelle_accent_chair.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Tartonelle Accent Chair').first()
    itemtag = item_tag(getitemid.item_id, 2)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 11)
    db.session.add(itemsubtag)

    item = item_info('Benches Upholstered Button-Tufted Storage Bench', "What a handsomely tailored upholstered storage bench. Black faux leather upholstery is elevated with button tufting. Lift the cushion to reveal ample storage for your pillows, throws and more."
                     , 169.99, "benches_upholstered_button-tufted_storage_bench.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Benches Upholstered Button-Tufted Storage Bench').first()
    itemtag = item_tag(getitemid.item_id, 2)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 11)
    db.session.add(itemsubtag)


    # Items for Bathroom
    item = item_info('Kasper 24" Single Bathroom Floating Vanity Set', "The contemporary simplicity of this floating bathroom vanity will add stunning modern flair to your bathroom or powder room. The open space below allows you to clean the floor with ease or stow the linen hamper, while double doors open to reveal plenty of storage space for all of your bathroom essentials. The clean lines that permeate through the design of this bathroom vanity will surely create a fresh look in your home."
                     , 274.99, "kasper_24_single_bathroom_floating_vanity_set.jpg")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Kasper 24" Single Bathroom Floating Vanity Set').first()
    itemtag = item_tag(getitemid.item_id, 3)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 13)
    db.session.add(itemsubtag)

    item = item_info('Southern Enterprises Corrine Italian Marble Bath Vanity Sink', "Step up your sink game with this small space vanity sink. Authentic, Italian marble top borders a ceramic sink, crafting a monochromatic look. Rich, dark sienna drawers and shelf enhance this modern wash station’s contemporary design. Upgrade your bathroom with this charming bathroom sink vanity."
                     , 228.98, "southern_enterprises_corrine_italian_marble_bath_vanity_sink.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Southern Enterprises Corrine Italian Marble Bath Vanity Sink').first()
    itemtag = item_tag(getitemid.item_id, 3)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 13)
    db.session.add(itemsubtag)


    item = item_info('Linon Bracken Tall Cabinet', "The Bracken tall cabinet takes advantage of vertical space providing ample storage and display space for linens and bathroom necessities. One door keeps the three lower shelves hidden, while three upper shelves are open for easy access. Crafted from solid bamboo, the piece is both sturdy and durable."
                     , 191.99, "linon_bracken_tall_cabinet.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Linon Bracken Tall Cabinet').first()
    itemtag = item_tag(getitemid.item_id, 3)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 14)
    db.session.add(itemsubtag)

    item = item_info('Safavieh 6-Tier Storage Chest', "Getting a little short on storage space? Look no further than this perfectly charming—and practical—6-basket storage shelf. The ideal way to organize any room in the house, six spacious woven baskets tuck neatly into a distressed black pine cabinet. As versatile as it is attractive, use it in place of a dresser, sideboard or TV stand for that much more cool character."
                     , 219.99, "safavieh_6_Tier_storage_chest.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Safavieh 6-Tier Storage Chest').first()
    itemtag = item_tag(getitemid.item_id, 3)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 14)
    db.session.add(itemsubtag)


    item = item_info('Contemporary Rust-Proof Over the Door Double Hook', "This over the door hanging rack works for every situation—whether you need to a temporary place to store your guest’s coat and handbag or want to keep your towels from cluttering the floor. What an instant, save-spacing solution. This double hook installs within minutes with no tools required."
                     , 25.99, "contemporary_rust-proof_over_the_door_double_hook.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Contemporary Rust-Proof Over the Door Double Hook').first()
    itemtag = item_tag(getitemid.item_id, 3)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 15)
    db.session.add(itemsubtag)

    item = item_info('Over-the-Door Double Hook Over the Door Hanging Rack', "There's no need to grab your power drill to instantly add storage space for your wardrobe. Simply attach this contemporary metal double hook to your bedroom or bathroom door and enjoy having everything within reach. The hook fits snugly over most standard doors and securely keeps clothing in place, freeing your floors from unsightly clutter. Great for the entryway, bedroom, and bathroom."
                     , 22.99, "over-the-door_double_hook_over_the_door_hanging_rack.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Over-the-Door Double Hook Over the Door Hanging Rack').first()
    itemtag = item_tag(getitemid.item_id, 3)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 15)
    db.session.add(itemsubtag)


    item = item_info('Horizon 4-Light LED Pendant', "Inspired by the clean lines of mid-century design, this linear pendant light features a rich, wood finish on its horizontal slats, where four LED Edison bulbs shine through to provide warm, ambient light. The adjustable-height metal frame has an understated, minimalistic look."
                     , 263.99, "horizon_4-light_LED_pendant.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Horizon 4-Light LED Pendant').first()
    itemtag = item_tag(getitemid.item_id, 3)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 16)
    db.session.add(itemsubtag)

    item = item_info('Vanity Art 3 Light Dimmable Vanity Light', "The warm light created by this unique 3-light vanity light, its exquisite design, and multi-functionalization, both exquisite and personalized. There is a horizontal fixed rod on a black round base, which connects three vortex-shaped lampshades. Each metal light shade is carefully designed. It requires three standard 60W bulbs (not included). You can install it in the bathroom, above the mirror, to achieve the decorative purpose you want. A two-year warranty is included."
                     , 109.99, "vanity_art_3_light_dimmable_vanity_light.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Vanity Art 3 Light Dimmable Vanity Light').first()
    itemtag = item_tag(getitemid.item_id, 3)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 16)
    db.session.add(itemsubtag)


    item = item_info('Embossed Mirror', "Style and prose? This accent mirror has it. The embossed, champagne color frame elegantly curves in all the right places. Everyone that comes to enjoy your talk-of-the-town dinner parties will appreciate this piece of glamour on your wall."
                     , 495.99, "A60003174_2.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Embossed Mirror').first()
    itemtag = item_tag(getitemid.item_id, 3)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 17)
    db.session.add(itemsubtag)

    item = item_info('Crosley Mirrored Wall Medicine Cabinet', "Not quite ready for the inconvenience and expense of a complete bathroom remodel? This line of stylish storage solutions will help you create the bathroom of your dreams. the high-end design of this wall medicine cabinet keeps your bathroom essentials and its true purpose cleverly under wraps. The mirrored cabinet door opens to reveal roomy storage space and three adjustable shelves. Its dual-purpose role as a mirror and cabinet allows you to live large in small spaces."
                     , 160.99, "A600000174_2.jpg")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Crosley Mirrored Wall Medicine Cabinet').first()
    itemtag = item_tag(getitemid.item_id, 3)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 17)
    db.session.add(itemsubtag)


    item = item_info('Laundry Station', "TRINITY's 3-Bag Bamboo Laundry Station is a great addition to any laundry, closet, bathroom, or bedroom area. The 100% pre-shrunk cotton bags are large enough to hold loads of all sizes, while allowing for easy sorting of all your laundry items. Use the handles to grab your laundry and go."    
                     , 161.99, "A600009949_2.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Laundry Station').first()
    itemtag = item_tag(getitemid.item_id, 3)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 18)
    db.session.add(itemsubtag)

    item = item_info('happimess Curtis 8 Gallon Trash Can', "This classic trash can combines quality construction with modern styling for your kitchen or office. A satin chrome-tone finish suits any decor and the tall, narrow shape fits easily into a small space. Dispose of trash hands-free with the convenient step pedal."    
                     , 95.99, "A600065541_1.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='happimess Curtis 8 Gallon Trash Can').first()
    itemtag = item_tag(getitemid.item_id, 3)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 18)
    db.session.add(itemsubtag)
    

    # Items for Kitchen
    item = item_info('Lyncott Extendable Dining Table', "A refreshed take on retro aesthetics. The Lyncott dining extension table adds an air of playful simplicity to your dining space, capturing the architectural language of mid-century stylings. Subtle in design, it invites the eye with a sleek, open frame. A casual, yet timeless, finish and self-storing extension leaf complete this study in form and function."    
                     , 319.00, "D615-35-ANGLE-ALT-SW-P1-KO.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Lyncott Extendable Dining Table').first()
    itemtag = item_tag(getitemid.item_id, 4)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 19)
    db.session.add(itemsubtag)

    item = item_info('Rencott Dining Extension Table', "The Rencott dining extension table's classic yet contemporary good looks are hard to deny. Its geometric double pedestal base is effortlessly eye-catching, while a metal inlay on the tabletop offers a subtly striking touch. With a light oak finish and wire-brushed wood grain texture, this table lends an organic appeal to your delicious dining space ... or wherever family and guests gather."    
                     , 949.99, "D781-35-ANGLE-SW-P1-KO.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Rencott Dining Extension Table').first()
    itemtag = item_tag(getitemid.item_id, 4)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 19)
    db.session.add(itemsubtag)


    item = item_info('Isanti Upholstered Dining Chair (Set of 2)', "With its back-to-nature sensibility, the Isanti dining room side chair is a natural fit for your well-edited space. A clean-lined design lets the beautifully organic quality and inherent luster of the wood shine through. From its textural upholstery to the refreshing light finish, it’s a piece that makes a statement by being remarkably understated."    
                     , 250.00, "D752-01(2)-SW-AGR.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Isanti Upholstered Dining Chair (Set of 2)').first()
    itemtag = item_tag(getitemid.item_id, 4)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 20)
    db.session.add(itemsubtag)

    item = item_info('Wildenauer Dining Chair (Set of 2)', "Raise the bar on modern farmhouse style with the Wildenaur dining side chair. Its casual good looks are accentuated with a handsome two-tone finish. A clean-lined silhouette with a modern ladderback design adds a fresh element, whether your style is vintage, country or eclectic. This richly crafted seating option serves up charm wherever folks decide to take a seat."    
                     , 159.98, "D634-01(2)-ANGLE-SW-P1-KO.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Wildenauer Dining Chair (Set of 2)').first()
    itemtag = item_tag(getitemid.item_id, 4)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 20)
    db.session.add(itemsubtag)

    
    item = item_info('Wildenauer 50" Dining Bench', "Raise the bar on modern farmhouse style with the Wildenaur dining bench. Its casual good looks are accentuated with a handsome two-tone finish. A sturdy silhouette adds a hearty element, whether your style is vintage, country or eclectic. This richly crafted seating option serves up charm wherever folks decide to take a seat."    
                     , 110.00, "D634-00-ANGLE-SW-P1-KO.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Wildenauer 50" Dining Bench').first()
    itemtag = item_tag(getitemid.item_id, 4)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 21)
    db.session.add(itemsubtag)

    item = item_info('Rencott 63" Dining Bench', "The Rencott dining bench's classic yet contemporary good looks are hard to deny. Its softly cushioned seat in a woven fabric adds a comfortably cozy dimension to everyday seating or when guests gather. With a light oak finish and wire-brushed wood grain texture, this bench lends an organic appeal to your delicious dining space ... or wherever family and guests gather."    
                     , 190, "D781-00-ANGLE-SW-P1-KO.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Rencott 63" Dining Bench').first()
    itemtag = item_tag(getitemid.item_id, 4)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 21)
    db.session.add(itemsubtag)


    item = item_info('Foyland Dining Server', "The Foyland dining room server is casual contemporary style simply done right. Its two-tone color scheme features a rich brushed black main color accented with a beautiful dusty grayish brown wood tone. The versatile piece features three center drawers and two more tucked neatly behind the doors, offering plenty of space to serve your storage needs with ease."    
                     , 999.99, "D989-60-ANGLE-CLSD-SW-P1-KO.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Foyland Dining Server').first()
    itemtag = item_tag(getitemid.item_id, 4)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 22)
    db.session.add(itemsubtag)

    item = item_info('Ashbryn Dining Server and Hutch', "The Ashbryn server and hutch delivers casual style with substance. A classic white finish and butcher block oak veneer top add a relaxed vibe to a delicious design that exudes a modern farmhouse aesthetic. Cabinets, drawers and open shelves provide ample storage and display space for dining essentials and decor. This charmingly curated piece is a show of great taste."    
                     , 1019.98, "D844-60-61-ANGLE-SW-P1-KO.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Ashbryn Dining Server and Hutch').first()
    itemtag = item_tag(getitemid.item_id, 4)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 22)
    db.session.add(itemsubtag)


    item = item_info('Southern Enterprises Furniture Bar Cabinet', "A swanky essential for the entertainer, this bar cabinet in dramatic black with red interior brings back cocktail hour in high style. Behind the double doors, you’ll find nine storage cubbies varying in size to store wine, liquor, glasses and whatever else you want to add to the mix. What a delicious addition to modern or mid-century inspired abodes."    
                     , 271.99, "D600000749_2.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Southern Enterprises Furniture Bar Cabinet').first()
    itemtag = item_tag(getitemid.item_id, 4)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 23)
    db.session.add(itemsubtag)

    item = item_info('Southern Enterprises Furniture Holmgren Rolling Wine Cart', "Gather friends and raise your glass with this modern bar cart—perfect for at-home get-togethers. Tray shelving ensures that glasses and utensils stay where they belong, and specially designed storage compartments easily hold wine glasses and bottles. Wheel this wine cart wherever the party may take you, from dining rooms and kitchens to open-concept living spaces."    
                     , 310.99, "D600001986_2.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Southern Enterprises Furniture Holmgren Rolling Wine Cart').first()
    itemtag = item_tag(getitemid.item_id, 4)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 23)
    db.session.add(itemsubtag)


    # Items for Office
    item = item_info('Roanhowe 68" Home Office Desk', "Give your mid-century modern decor that finishing touch with the Roanhowe home office desk. Spacious drawers with unique wooden drawer pulls enhance the design with stunning style. This desk takes minimalism to the max."    
                     , 779.99, "H769-21-ANGLE-SW-P1-KO.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Roanhowe 68" Home Office Desk').first()
    itemtag = item_tag(getitemid.item_id, 5)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 25)
    db.session.add(itemsubtag)

    item = item_info('Montia 67" Home Office Desk', "Sleek in its simplicity, the Montia home office desk encourages you to work or study in style. Its mixed-material design brings a trendy, urban chic feel to your work area. Functional features keep the desk top clutter-free—easily tuck away essentials in the three drawers, and conceal power cords with the open raceway."    
                     , 429.99, "H632-44-ANGLE-SW-P1-KO.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Montia 67" Home Office Desk').first()
    itemtag = item_tag(getitemid.item_id, 5)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 25)
    db.session.add(itemsubtag)


    item = item_info('Montia Home Office Desk Chair', "Sleek in its simplicity, the Montia home office desk chair encourages you to work or study in style. Its mixed-material design brings a trendy, urban chic feel to your work area. With this contemporary piece, form and function are never far apart."    
                     , 149.99, "H632-01A-ANGLE-SW-P1-KO.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Montia Home Office Desk Chair').first()
    itemtag = item_tag(getitemid.item_id, 5)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 26)
    db.session.add(itemsubtag)

    item = item_info('Modway Veer Mesh Office Chair', "Chart new territory while seated from the comfort of the Veer chair. It features a form-fitted breathable mesh back and padded waterfall mesh seat to keep your back and thighs posture perfect. Easily flip the padded armrests up and away when not needed with the chair's versatile 90-degree rotating feature. Securely lock your back in place with a user-friendly seat tilt plus tension control knob, perfect for adjusting the chair to correctly fit your body weight. Adjust the seat height with a one-touch pneumatic lift, while hooded dual-wheel casters to ensure effortless gliding over carpeted offices."    
                     , 150.99, "H600003648_2.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Modway Veer Mesh Office Chair').first()
    itemtag = item_tag(getitemid.item_id, 5)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 26)
    db.session.add(itemsubtag)


    item = item_info('Beckincreek Large Bookcase with 5 Shelves', "Make a style statement with the Beckincreek large bookcase. Its traditional design is updated with an on trend vintage black finish. The bookcase's five shelves add up to a well-organized workspace."    
                     , 379.99, "H778-17-ANGLE-SW-P1-KO.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Beckincreek Large Bookcase with 5 Shelves').first()
    itemtag = item_tag(getitemid.item_id, 5)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 27)
    db.session.add(itemsubtag)

    item = item_info('Bernmore 63" Corner Shelf Bookcase', "Books, decorative pieces or personal photos shine when displayed on this Bernmore corner shelf. Five shelves allow you to achieve a layered style while also offering an efficient storage solution. The black finish makes this a versatile piece perfect for any room in the house."    
                     , 139.99, "A4000304-HEAD-ON-SW-P1-KO.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Bernmore 63" Corner Shelf Bookcase').first()
    itemtag = item_tag(getitemid.item_id, 5)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 27)
    db.session.add(itemsubtag)


    item = item_info('Harlow Sideboard Storage Cabinet', "Whether you prefer Scandinavian style or mid-century modern, this storage cabinet is loaded with possibilities. Distinctive canted legs complement the white and walnut contrast tones for a design steeped in retro. A roomy shelved cabinet reveals ample stowaway space, while three smooth-gliding drawers keep linens and what-nots in place. Streamlined style works well whether rooted in the entryway, dining room or den."    
                     , 234.98, "H600000050-SW-KO.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Harlow Sideboard Storage Cabinet').first()
    itemtag = item_tag(getitemid.item_id, 5)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 28)
    db.session.add(itemsubtag)

    item = item_info('Camiburg 2 Drawer File Cabinet', "Whether you lean towards modern farmhouse or urban industrial design, the clean-lined profile of the Camiburg file cabinet is an essential component to any well-equipped home office. Sleek and slim, it’s just enough furniture to complete your space without overloading your look."    
                     , 129.98, "H283-12-ANGLE-SW-P1-KO.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Camiburg 2 Drawer File Cabinet').first()
    itemtag = item_tag(getitemid.item_id, 5)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 28)
    db.session.add(itemsubtag)


    item = item_info('Barolli 60" Gaming Desk with Monitor Stand', "Elevate your style and up your game with the ultra-cool Barolli gaming desk. Clean and contemporary, this mixed-media designer desk includes a metal frame in a gunmetal finish, topped with an engineered wood surface with replicated wood grain. Setting you up for success: a large open raceway for power cord management, a desktop monitor shelf, and an LED back light with multiple color options for an enhanced gaming experience. Along with a PC stand for easy access, this gaming desk features a custom designed headset hanger and a built-in electric can cooler with a USB plug-in."    
                     , 439.98, "H700-28-ANGLE-SW-P1-KO.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Barolli 60" Gaming Desk with Monitor Stand').first()
    itemtag = item_tag(getitemid.item_id, 5)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 29)
    db.session.add(itemsubtag)

    item = item_info('Techni Sport Gaming Chair', "Ergonomic, high back, sleek and in kawaii style, a perfect choice for your gaming room or game station. Designed to provide an extra comfort during your gaming sessions with its neck pillow and heart shaped plush cushion for lumbar support. Made with rich and high quality PU, memory foam seat and iridescent trim outlining the seat enhances your gaming experience. Features steel structure, pneumatic seat height adjustment, tilt with tension lock mechanism, 150 degree reclining mechanism, 2D adjustable white padded armrests and 5-star durable white nylon base, non-marking casters, we got you covered. This chair supports the weight limit of 250lbs and comes with limited warranty."    
                     , 309.98, "H600002326_2.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Techni Sport Gaming Chair').first()
    itemtag = item_tag(getitemid.item_id, 5)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 29)
    db.session.add(itemsubtag)


    # Items for Outdoor
    item = item_info('Cherry Point Nuvella Outdoor 4 Piece Sectional Set', "Turn your outdoor space into a sweet retreat with the Cherry Point 4-piece outdoor sectional. High style crafted for low-maintenance living, this decidedly clean and contemporary outdoor furniture set entices in an easy-breezy gray resin wicker over a rust-free aluminum frame for an upscale aesthetic that’s downright durable. Wrapped in high-performing Nuvella® fabric, the plush cushions are indulgently comfortable yet so carefree."    
                     , 999.98, "P301-070-ANGLE-A-SW-P1-KO.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Cherry Point Nuvella Outdoor 4 Piece Sectional Set').first()
    itemtag = item_tag(getitemid.item_id, 6)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 31)
    db.session.add(itemsubtag)

    item = item_info('Beachcroft Nuvella Outdoor Sofa', "Sporting an easy-on-the-eyes look inspired by driftwood, the Beachcroft sofa elevates the art of indoor-outdoor living. Beautiful and durable enough for indoor and outdoor use, this high-style/low-maintenance sofa entices with plush, removable cushions wrapped in Nuvella® fabric that’s a breeze to keep clean."    
                     , 1199.99, "P791-838-ANGLE-SW-P1-KO.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Beachcroft Nuvella Outdoor Sofa').first()
    itemtag = item_tag(getitemid.item_id, 6)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 31)
    db.session.add(itemsubtag)


    item = item_info('Beachcroft Outdoor Chaise Lounge with Nuvella Cushion', "Sporting an easy-on-the-eyes look inspired by driftwood, the easily adjustable Beachcroft chaise lounge elevates the art of indoor-outdoor living. Beautiful and durable enough for indoor and outdoor use, this high-style/low-maintenance lounger entices with a plush, removable cushion wrapped in Nuvella® fabric that’s a breeze to keep clean."    
                     , 439.99, "P791-815-ANGLE-UP-SW-P1-KO.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Beachcroft Outdoor Chaise Lounge with Nuvella Cushion').first()
    itemtag = item_tag(getitemid.item_id, 6)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 32)
    db.session.add(itemsubtag)

    item = item_info('Emmeline Outdoor Lounge Chair Set of 2 with Nuvella Cushions', "Get back to nature with the relaxed styling of the Emmeline outdoor lounge chair with cushion. Crafted of MEGA TUFF™ HDPE material, it combines the exceptional durability and weather resistance you need with the “wood look” you love. Rest assured, the cushions are wrapped in comfortable and carefree Nuvella® fabric, leaving you plenty of time to sit back and smell the roses."    
                     , 999.99, "P420-820(2)-SW-P1-KO.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Emmeline Outdoor Lounge Chair Set of 2 with Nuvella Cushions').first()
    itemtag = item_tag(getitemid.item_id, 6)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 32)
    db.session.add(itemsubtag)


    item = item_info('Beachcroft Outdoor Dining Table and 4 Chairs and Bench', "Sporting an easy-on-the-eyes look inspired by driftwood, the Beachcroft dining set elevates the art of alfresco living. Beautiful and durable enough for indoor or outdoor use, the pieces blend high style with low maintenance. The table charms with X-leg farmhouse styling and a thick porcelain table top that’s a natural complement. The brilliantly styled bench and chairs entice with a plush, removable cushion wrapped in high-performing Nuvella® fabric that’s a breeze to keep clean."    
                     , 2849.99, "P791-625-601-601A-600-SW-P1-KO.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Beachcroft Outdoor Dining Table and 4 Chairs and Bench').first()
    itemtag = item_tag(getitemid.item_id, 6)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 33)
    db.session.add(itemsubtag)

    item = item_info('Town Wood Outdoor 3-Piece Dining Set', "Bring an uptown feel to an outdoor space with the Town Wood outdoor furniture set. Designed to comfortably seat four, this ultra-cool outdoor dining table and bench set a new standard in outdoor living. The tabletop and bench seats are richly crafted of acacia wood with wonderful tonal variation. Tubular steel legs are sleek, sturdy and slightly canted for an interesting angled effect."    
                     , 399.99, "P220-115-ANGLE-SW-P1-KO.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Town Wood Outdoor 3-Piece Dining Set').first()
    itemtag = item_tag(getitemid.item_id, 6)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 33)
    db.session.add(itemsubtag)


    item = item_info('Paradise Trail Outdoor Fire Pit Table', "Turn your backyard space into your own piece of paradise with the Paradise Trail outdoor table with fire pit. Though this outdoor table looks remarkably like wood, it’s made of sturdy, rust-proof aluminum that’s perfectly suited for alfresco living. Enhancing the rustically refined aesthetic: side panels accented with all-weather, handwoven resin wicker. The result may look high maintenance, but rest assured, this outdoor fire pit table is anything but. With the press of a button, ignite a flickering flame that dances over a bed of glass beads. And with room for up to eight, it’s one highly accommodating outdoor bar table."    
                     , 1099.99, "P750-776-CLSD-ANGLE-SW-P1-KO.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Paradise Trail Outdoor Fire Pit Table').first()
    itemtag = item_tag(getitemid.item_id, 6)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 34)
    db.session.add(itemsubtag)

    item = item_info('Solo Stove Ranger 2.0 15" Fire Pit', "This fire pit is sized for every adventure. Easily light up a smokeless fire anywhere life takes you thanks to its compact size."    
                     , 199.99, "P600009377_2.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Solo Stove Ranger 2.0 15" Fire Pit').first()
    itemtag = item_tag(getitemid.item_id, 6)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 34)
    db.session.add(itemsubtag)


    item = item_info('Furinno Tioman Outdoor Swing with Stand', "The Furinno Tioman hanging porch swing brings the relaxed lifestyle from the tropical islands to your backyard. Whether you want to enjoy a cup of coffee with your loved ones while watching the sunset or read a book alone on a warm afternoon, this porch swing suits your needs while staying in your budget. Manufactured from Malaysian dark red Meranti wood and treated with teak oil, this bench is durable and water-resistant. Simple in design, this swing is great for your porch, backyard, garden or patio."    
                     , 209.99, "P600005217_2.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Furinno Tioman Outdoor Swing with Stand').first()
    itemtag = item_tag(getitemid.item_id, 6)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 35)
    db.session.add(itemsubtag)

    item = item_info('Bayberry Lane Outdoor Flamingo Garden Sculpture (Set of 2)', "Add coastal flair to your home with this vibrant set of two flamingo sculptures. These figurines are bound to impress your guests with their marvelous design and uniqueness. Made of iron and showcasing impressive hand-painted floral patterns and multicolor finishes, each feathered friend features detailed characteristics and metal feet that serve as a sturdy base. What a charming way to add an artistic twist to your favorite indoor or outdoor spaces."    
                     , 110.99, "P600005420_2.webp")
    db.session.add(item)
    getitemid = item_info.query.filter_by(item_name='Bayberry Lane Outdoor Flamingo Garden Sculpture (Set of 2)').first()
    itemtag = item_tag(getitemid.item_id, 6)
    db.session.add(itemtag)
    itemsubtag = item_subtag(getitemid.item_id, 35)
    db.session.add(itemsubtag)

    db.session.commit()

def create_category():
    tag = tag_list('Living Room', 'Furniture for living room', 'living_room_cat.webp')
    db.session.add(tag)

    tag = tag_list('Bedroom', 'Furniture for bedroom', 'bedroom_cat.webp')
    db.session.add(tag)

    tag = tag_list('Bathroom', 'Furniture for bathroom', 'bathroom_cat.webp')
    db.session.add(tag)

    tag = tag_list('Kitchen', 'Furniture for kitchen', 'kitchen_cat.webp')
    db.session.add(tag)

    tag = tag_list('Office', 'Furniture for office', 'office_cat.webp')
    db.session.add(tag)

    tag = tag_list('Outdoor', 'Furniture for outdoor', 'outdoor_cat.webp')
    db.session.add(tag)

    db.session.commit()

def create_subcategory():
    subtag = subtag_list('Sofas & Couches', 'Living Room', 'subcategory for Living Room', 'sofas_n_couches_cat.webp')
    db.session.add(subtag)

    subtag = subtag_list('Recliners', 'Living Room', 'subcategory for Living Room', 'recliners_cat.webp')
    db.session.add(subtag)

    subtag = subtag_list('Accent Chairs', 'Living Room', 'subcategory for Living Room', 'accent_chairs_cat.webp')
    db.session.add(subtag)

    subtag = subtag_list('Coffee Tables', 'Living Room', 'subcategory for Living Room', 'coffe_tables_cat.webp')
    db.session.add(subtag)

    subtag = subtag_list('TV Stands', 'Living Room', 'subcategory for Living Room', 'tv_stands_cat.webp')
    db.session.add(subtag)

    subtag = subtag_list('More Living Room Options', 'Living Room', 'subcategory for Living Room', 'more_options_cat.jpg')
    db.session.add(subtag)


    subtag = subtag_list('Beds', 'Bedroom', 'subcategory for Bedroom', 'beds_cat.webp')
    db.session.add(subtag)
    
    subtag = subtag_list('Bedding', 'Bedroom', 'subcategory for Bedroom', 'bedding_cat.webp')
    db.session.add(subtag)

    subtag = subtag_list('Dressers', 'Bedroom', 'subcategory for Bedroom', 'dressers_cat.webp')
    db.session.add(subtag)

    subtag = subtag_list('Nightstands', 'Bedroom', 'subcategory for Bedroom', 'nightstands_cat.webp')
    db.session.add(subtag)

    subtag = subtag_list('Bedroom Chairs', 'Bedroom', 'subcategory for Bedroom', 'bedroom_chairs_cat.webp')
    db.session.add(subtag)

    subtag = subtag_list('More Bedroom Options', 'Bedroom', 'subcategory for Bedroom', 'bedroom_more_options_cat.webp')
    db.session.add(subtag)


    subtag = subtag_list('Bathroom Vanities', 'Bathroom', 'subcategory for Bathroom', 'bathroom_vanities_cat.webp')
    db.session.add(subtag)
    
    subtag = subtag_list('Bathroom Storage', 'Bathroom', 'subcategory for Bathroom', 'bathroom_storage_cat.webp')
    db.session.add(subtag)

    subtag = subtag_list('Bathroom Fixtures', 'Bathroom', 'subcategory for Bathroom', 'bathroom_fixtures_cat.webp')
    db.session.add(subtag)

    subtag = subtag_list('Bathroom Lighting', 'Bathroom', 'subcategory for Bathroom', 'bathroom_lighting_cat.webp')
    db.session.add(subtag)

    subtag = subtag_list('Bedroom Mirrors', 'Bathroom', 'subcategory for Bathroom', 'bathroom_mirrors_cat.webp')
    db.session.add(subtag)

    subtag = subtag_list('Bathroom Wastebaskets & Hampers', 'Bathroom', 'subcategory for Bathroom', 'bathroom_waste_hampers_cat.webp')
    db.session.add(subtag)


    subtag = subtag_list('Dining Tables', 'Kitchen', 'subcategory for Kitchen', 'dining_tables_cat.webp')
    db.session.add(subtag)
    
    subtag = subtag_list('Dining Chairs', 'Kitchen', 'subcategory for Kitchen', 'dining_chairs_cat.webp')
    db.session.add(subtag)

    subtag = subtag_list('Dining Benches', 'Kitchen', 'subcategory for Kitchen', 'dining_benches_cat.webp')
    db.session.add(subtag)

    subtag = subtag_list('Dining Storage', 'Kitchen', 'subcategory for Kitchen', 'dining_storage_cat.webp')
    db.session.add(subtag)

    subtag = subtag_list('Bar Furniture', 'Kitchen', 'subcategory for Kitchen', 'bar_furniture_cat.webp')
    db.session.add(subtag)

    subtag = subtag_list('More Dining Options', 'Kitchen', 'subcategory for Kitchen', 'kitchen_more_options_cat.webp')
    db.session.add(subtag)


    subtag = subtag_list('Office Desks', 'Office', 'subcategory for Office', 'office_desks_cat.webp')
    db.session.add(subtag)
    
    subtag = subtag_list('Office Chairs', 'Office', 'subcategory for Office', 'office_chairs_cat.webp')
    db.session.add(subtag)

    subtag = subtag_list('Bookcases', 'Office', 'subcategory for Office', 'bookcases_cat.webp')
    db.session.add(subtag)

    subtag = subtag_list('Office Storage', 'Office', 'subcategory for Office', 'office_storage_cat.webp')
    db.session.add(subtag)

    subtag = subtag_list('Gaming', 'Office', 'subcategory for Office', 'gaming_cat.webp')
    db.session.add(subtag)

    subtag = subtag_list('More Office Options', 'Office', 'subcategory for Office', 'office_more_options_cat.webp')
    db.session.add(subtag)


    subtag = subtag_list('Outdoor Sofas', 'Outdoor', 'subcategory for Outdoor', 'outdoor_sofas_cat.webp')
    db.session.add(subtag)
    
    subtag = subtag_list('Outdoor Chairs', 'Outdoor', 'subcategory for Outdoor', 'outdoor_chairs_cat.webp')
    db.session.add(subtag)

    subtag = subtag_list('Outdoor Dining', 'Outdoor', 'subcategory for Outdoor', 'outdoor_dining_cat.webp')
    db.session.add(subtag)

    subtag = subtag_list('Outdoor Heating', 'Outdoor', 'subcategory for Outdoor', 'outdoor_heating_cat.webp')
    db.session.add(subtag)

    subtag = subtag_list('Outdoor Decor', 'Outdoor', 'subcategory for Outdoor', 'outdoor_decor_cat.webp')
    db.session.add(subtag)

    subtag = subtag_list('Outdoor Deals', 'Outdoor', 'subcategory for Outdoor', 'outdoor_deals_cat.webp')
    db.session.add(subtag)

    db.session.commit()