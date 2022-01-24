# 等额本息（均使用基准利率）
# 组合贷可作为课后习题
# 商业贷款利率：4.9%
# 公积金利率：3.25%

# 每月还款额=贷款本金×[月利率×(1+月利率) ^ 还款月数]÷{[(1+月利率) ^ 还款月数]-1}
while True:
    loan_type = input("请选择贷款类型：1.商业贷款  2.公积金贷款  3.组合贷款\n")
    # 贷款金额
    if loan_type != '3':
        loan_amount = float(input("请输入贷款金额（万）\n"))
        term = int(input("请选择期限（年）：5、10、15、20、25\n"))
        if term in [5,10,15,20,25]:
            if term==5:
                mon_rate = (4.75 / 100) / 12  # 计算月利率
                # 计算每月应还金额
                mon_pay = loan_amount * 10000 * (mon_rate * ((1 + mon_rate) ** (term * 12))) / (
                        ((1 + mon_rate) ** (term * 12)) - 1)
                # 计算还款总额
                all_pay = mon_pay * term * 12
                # 计算支付利息
                interest = all_pay - loan_amount * 10000
                print("每月月供参考（元）：{:.2f}元".format(mon_pay))
                print("支付利息（元）：{:.2f}元".format(interest))
                print("还款总额（元）：{:.2f}元".format(all_pay))

            else:
                # 商业贷款
                if loan_type == '1':  # 商业贷款
                    mon_rate = (4.90 / 100) / 12  # 计算月利率
                    # 计算每月应还金额
                    mon_pay = loan_amount * 10000 * (mon_rate * ((1 + mon_rate) ** (term * 12))) / (
                            ((1 + mon_rate) ** (term * 12)) - 1)
                    # 计算还款总额
                    all_pay = mon_pay * term * 12
                    # 计算支付利息
                    interest = all_pay - loan_amount * 10000
                    print("每月月供参考（元）：{:.2f}元".format(mon_pay))
                    print("支付利息（元）：{:.2f}元".format(interest))
                    print("还款总额（元）：{:.2f}元".format(all_pay))

                elif loan_type == '2':  # 公积金贷款
                    if term==5:
                        mon_rate = (2.75 / 100) / 12  # 计算月利率
                    else:
                        mon_rate = (3.25 / 100) / 12  # 计算月利率
                        # 计算每月应还金额
                    mon_pay = loan_amount * 10000 * (mon_rate * ((1 + mon_rate) ** (term * 12))) / (
                            ((1 + mon_rate) ** (term * 12)) - 1)
                    # 计算还款总额
                    all_pay = mon_pay * term * 12
                    # 计算支付利息
                    interest = all_pay - loan_amount * 10000
                    print("每月月供参考（元）：{:.2f}元".format(mon_pay))
                    print("支付利息（元）：{:.2f}元".format(interest))
                    print("还款总额（元）：{:.2f}元".format(all_pay))
        else:
            print('请输入合法的期限')
    else:
        # 商贷金额
        business_loan = float(input("请输入商业贷款金额（万）：\n"))
        # 公积金贷款
        fund_loan = float(input("请输入公积金贷款金额（万）：\n"))
        term = int(input("请选择期限（年）：5、10、15、20、25\n"))
        if term in [5, 10, 15, 20, 25]:
            if term ==5:
                business_mon_rate = (4.75 / 100) / 12  # 商贷月利率
                found_mon_rate = (2.75 / 100) / 12  # 公积金月利率
            else:

                business_mon_rate = (4.90 / 100) / 12  # 商贷月利率
                found_mon_rate = (3.25 / 100) / 12  # 公积金月利率
            # 计算商业贷款 每月应还金额
            business_mon_pay = business_loan * 10000 * (business_mon_rate * ((1 + business_mon_rate) ** (term * 12))) / (
                    ((1 + business_mon_rate) ** (term * 12)) - 1)
            # 计算公积金贷款 每月应还金额
            found_mon_pay = fund_loan * 10000 * (found_mon_rate * ((1 + found_mon_rate) ** (term * 12))) / (
                    ((1 + found_mon_rate) ** (term * 12)) - 1)
            # 每月总应还
            mon_all_pay = business_mon_pay + found_mon_pay

            all_pay = mon_all_pay * term * 12
            # 计算支付利息
            interest = all_pay - (business_loan + fund_loan)*10000
            print("每月月供参考（元）：{:.2f}元".format(mon_all_pay))
            print("支付利息（元）：{:.2f}元".format(interest))
            print("还款总额（元）：{:.2f}元".format(all_pay))
        else:
            print('请输入合法的期限')
