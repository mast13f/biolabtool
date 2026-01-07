# MALDI Metabolomics Database System

Automatically extract MALDI imaging figures from scientific PDFs, identify m/z annotations, and build a searchable CSV database.

## Installation

```bash
pip install anthropic pandas pymupdf
export ANTHROPIC_API_KEY='your-api-key'
```

## Quick Start

```python
from pdf_extractor import MALDIFigureExtractor
from database_builder import MALDIDatabase

# Extract figures
extractor = MALDIFigureExtractor()
extractor.extract_from_pdf("paper.pdf", output_folder="figures")

# Build database
db = MALDIDatabase("database.csv")
db.batch_process("figures/", literature_source="DOI: 10.1038/xxxxx")
db.save()

# Search
results = db.search_by_mz("885.5", tolerance=0.5)
```

## Files

- `pdf_extractor.py` - Extract MALDI figures from PDFs
- `database_builder.py` - Manage m/z and metabolite database
- `sample_usage.py` - Complete workflow example

## How It Works

### MALDI Image Detection

Claude AI identifies MALDI figures by looking for:
- Spatial distribution heatmaps on tissue
- m/z value annotations
- Color-coded intensity maps
- Multiple panels with different m/z values
- Keywords: MALDI, MSI, IMS

**What gets identified:**
- ✓ Tissue heatmaps with m/z labels → MALDI
- ✓ Multi-panel ion intensity maps → MALDI
- ✗ Regular microscopy → Not MALDI
- ✗ Western blots → Not MALDI

**Confidence threshold:** Default 70% (adjustable)

### Extraction Methods

1. **Embedded images** - Extract images directly from PDF
2. **Page rendering** - Render pages at 300 DPI (captures vector graphics)

Both methods ensure no MALDI figures are missed.

## Command Line

```bash
python pdf_extractor.py paper1.pdf paper2.pdf
# Output: extracted_maldi_figures/
```

## Usage

See `sample_usage.py` for complete workflow.

## Features

✅ Automatic MALDI detection via Claude AI  
✅ Confidence scoring  
✅ Dual extraction (embedded + rendered)  
✅ Batch processing  
✅ CSV database management  
✅ Tolerance-based m/z search  

## Troubleshooting

**No figures extracted**
- Check if PDF contains MALDI images
- Lower threshold: `confidence_threshold=50.0`

**Wrong images extracted**
- Raise threshold: `confidence_threshold=80.0`

**Inaccurate m/z extraction**
- Use higher resolution PDFs
- Manually edit CSV
