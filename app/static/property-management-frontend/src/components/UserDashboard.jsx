import React, { useState, useEffect } from 'react';
import { Card, Metric, Text } from '@tremor/react';
import { Table, TableBody, TableCell, TableHead, TableHeaderCell, TableRow } from '@tremor/react';


const UserDashboard = () => {
  const [paymentsCount, setPaymentsCount] = useState(0);
  const [paymentMethods, setPaymentMethods] = useState([]);
  const [totalBalance, setTotalBalance] = useState(0);
  const [latestPayments, setLatestPayments] = useState([]);

  useEffect(() => {
    fetchPaymentsCount();
    fetchPaymentMethods();
    fetchTotalBalance();
    fetchLatestPayments();
  }, []);

  const fetchPaymentsCount = async () => {
    try {
      const response = await fetch(`/payments/count`);
      const data = await response.json();
      console.log('Payments count:', data);
      setPaymentsCount(data.count);
    } catch (error) {
      console.error('Error fetching payments count:', error);
    }
  };

  const fetchPaymentMethods = async () => {
    try {
      const response = await fetch(`/payments/paymentmethods`);
      const data = await response.json();
      console.log('Payment methods:', data);
      setPaymentMethods(data.payment_methods);
    } catch (error) {
      console.error('Error fetching payment methods:', error);
    }
  };

  const fetchTotalBalance = async () => {
    try {
      const response = await fetch(`/payments/getbalance/tenant_id`);
      const data = await response.json();
      console.log('Total balance:', data);
      setTotalBalance(data.balance);
    } catch (error) {
      console.error('Error fetching total balance:', error);
    }
  };

  const fetchLatestPayments = async () => {
    try {
      const response = await fetch(`/payments`);
      const data = await response.json();
      console.log('Latest payments:', data);
      setLatestPayments(data);
    } catch (error) {
      console.error('Error fetching latest payments:', error);
    }
  };

  return (
    <div className="mx-auto max-w-2xl">
      {/* Card 1 */}
      <Card className="mx-auto max-w-xs" decoration="top" decorationColor="indigo">
        <p className="text-tremor-default text-tremor-content dark:text-dark-tremor-content">Payments Count</p>
        <p className="text-3xl text-tremor-content-strong dark:text-dark-tremor-content-strong font-semibold">{paymentsCount}</p>
      </Card>
      
      {/* Card 2 */}
      <Card className="mx-auto max-w-xs" decoration="top" decorationColor="indigo">
        <p className="text-tremor-default text-tremor-content dark:text-dark-tremor-content">Payment Methods</p>
        <ul>
          {paymentMethods.map((method, index) => (
            <li key={index}>{method.payment_method}: ${method.total}</li>
          ))}
        </ul>
      </Card>
      
      {/* Card 3 */}
      <Card className="mx-auto max-w-xs" decoration="top" decorationColor="indigo">
        <p className="text-tremor-default text-tremor-content dark:text-dark-tremor-content">Total Balance</p>
        <p className="text-3xl text-tremor-content-strong dark:text-dark-tremor-content-strong font-semibold">${totalBalance}</p>
      </Card>
      
      {/* Table */}
      <Table>
        <TableHead>
          <TableRow>
            <TableHeaderCell>Payment ID</TableHeaderCell>
            <TableHeaderCell>Tenant ID</TableHeaderCell>
            <TableHeaderCell>Amount</TableHeaderCell>
            <TableHeaderCell>Status</TableHeaderCell>
            <TableHeaderCell>Payment Type</TableHeaderCell>
            <TableHeaderCell>Description</TableHeaderCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {latestPayments.slice(0, 20).map(payment => (
            <TableRow key={payment.payment_id}>
              <TableCell>{payment.payment_id}</TableCell>
              <TableCell>{payment.tenant_id}</TableCell>
              <TableCell>{payment.amount}</TableCell>
              <TableCell>{payment.status}</TableCell>
              <TableCell>{payment.payment_type}</TableCell>
              <TableCell>{payment.description}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
}

export default UserDashboard;
