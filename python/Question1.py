def question01(initialLevelOfDebt, interestPercentage, repaymentPercentage):
    # modify and then return the variable below
  answer = 0.1 * initialLevelOfDebt;
  debt = initialLevelOfDebt;
  emi = initialLevelOfDebt * (repaymentPercentage / 100) if initialLevelOfDebt * (repaymentPercentage / 100) > 50 else 50;
  while debt > 0:
    debt = round(debt * 1.05, 2)
    if debt < emi:
      answer = answer + debt;
      debt = 0;
      break;
    debt = debt - emi;
    answer = answer + emi;
  return int(answer / 10) * 10;
