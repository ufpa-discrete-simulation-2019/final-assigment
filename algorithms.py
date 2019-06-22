def fso(sectors, floor):
  selected_car = None
  
  for sector in sectors:
    if sector.has_floor(floor):
      selected_car = sector.assigned_car

  lowest_sector = None

  for sector in sectors:
    if (not sector.is_vacant()) and sector.is_highest:
      sector_above = sector.sector_above

      if not sector_above.is_vacant() and sector_above.has_floor(floor):
        selected_car = sector.assigned_car
    
    if lowest_sector == None and (not sector.is_vacant()):
      if not sector.is_lowest:
        sector_below = sector.sector_below

        if sector_below.is_vacant() and sector_below.has_floor(floor):
          selected_car = sector.assigned_car
        
        lowest_sector = True
  
  return selected_car