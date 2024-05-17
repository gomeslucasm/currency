from fastapi import APIRouter, HTTPException, Query
from app.schemas.conversion import ALLOWED_CONVERSION_TYPES, ConversionResponse
from app.services.conversion import get_conversion_service


router = APIRouter()


@router.get("/convert", response_model=ConversionResponse)
async def convert_currency(
    from_currency: ALLOWED_CONVERSION_TYPES = Query(..., alias="from"),
    to_currency: ALLOWED_CONVERSION_TYPES = Query(..., alias="to"),
    amount: float = Query(..., gt=0),
):
    try:
        service = get_conversion_service()
        result = service.convert(from_currency, to_currency, amount)
        return ConversionResponse(
            from_currency=from_currency,
            to_currency=to_currency,
            original_amount=amount,
            converted_amount=result,
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
