from flask_smorest import Blueprint
from flask.views import MethodView
from marshmallow import Schema, fields

# PUBLIC_INTERFACE
class GalleryItemSchema(Schema):
    """Gallery item schema representing an image and metadata."""
    id = fields.Int(required=True, description="Unique identifier for the gallery item")
    title = fields.Str(required=True, description="Title of the gallery item")
    description = fields.Str(required=False, allow_none=True, description="Short description")
    imageUrl = fields.Url(required=True, description="Absolute or relative URL to the image")
    thumbnailUrl = fields.Url(required=False, allow_none=True, description="URL to thumbnail image")

# PUBLIC_INTERFACE
class GalleryListResponseSchema(Schema):
    """Response schema for a list of gallery items."""
    items = fields.List(fields.Nested(GalleryItemSchema), required=True, description="List of gallery items")

blp = Blueprint(
    "Gallery",
    "gallery",
    url_prefix="/api/gallery",
    description="Endpoints to retrieve gallery images and metadata"
)

@blp.route("/")
class GalleryList(MethodView):
    """Retrieve the list of gallery items."""
    # PUBLIC_INTERFACE
    @blp.doc(summary="List gallery items", description="Returns a list of gallery items for the portfolio website.")
    @blp.response(200, GalleryListResponseSchema)
    def get(self):
        """Return gallery items."""
        # For now we return a static list; later this can be replaced by DB or storage.
        items = [
            {
                "id": 1,
                "title": "Bharatanatyam Pose",
                "description": "A classical Bharatanatyam pose highlighting mudras.",
                "imageUrl": "https://images.unsplash.com/photo-1580137673164-c6ca47b462e1?q=80&w=1470&auto=format&fit=crop",
                "thumbnailUrl": "https://images.unsplash.com/photo-1580137673164-c6ca47b462e1?q=80&w=400&auto=format&fit=crop"
            },
            {
                "id": 2,
                "title": "Performance Stage",
                "description": "Live stage performance with traditional attire.",
                "imageUrl": "https://images.unsplash.com/photo-1482961674540-0b0e8363a005?q=80&w=1470&auto=format&fit=crop",
                "thumbnailUrl": "https://images.unsplash.com/photo-1482961674540-0b0e8363a005?q=80&w=400&auto=format&fit=crop"
            }
        ]
        return {"items": items}
